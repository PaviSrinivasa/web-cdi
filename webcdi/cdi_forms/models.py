# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_comma_separated_integer_list,MaxValueValidator,MinValueValidator,RegexValidator
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


class requests_log(models.Model):
    url_hash = models.CharField(max_length=128)
    request_type = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now = True)

# Method for ensuring that a value is positive
def validate_g_zero(value):
        if value <= 0:
            raise ValidationError("Value should be greater than 0")

# Method for ensuring that a value is not negative
def validate_ge_zero(value):
        if value < 0:
            raise ValidationError("Value should be greater than or equal to 0")

# Method for ensuring that a value is not zero
def validate_ne_zero(value):
        if value ==  0:
            raise ValidationError("Value should be non-zero")

#Method for formatting integers according to U.S. currency formats.
def format_currency(val):
    return "${:,}".format(val)

class Choices(models.Model):
    choice_set = models.CharField(max_length=101)
    def __str__(self):
        return self.choice_set

#Model for storing CDI items for all forms. Each row represents a single item for a single type of CDI questionnaire and its descriptive variables     
class Instrument_Forms(models.Model):
    instrument = models.ForeignKey('researcher_UI.instrument', db_index=True, on_delete=models.CASCADE)
    itemID = models.CharField(max_length = 101, db_index=True) # ID number for identification
    item = models.CharField(max_length = 101) # string variable name
    item_type = models.CharField(max_length = 101) # type of variable (word, phrase, etc.)
    category = models.CharField(max_length = 101) # if word, the subcategory for item (animals, sounds, etc.)
    choices = models.ForeignKey('Choices', null=True, on_delete=models.deletion.CASCADE)
    definition = models.CharField(max_length = 1001, null=True, blank=True) # item listed in plaintext. This is what is displayed to test-takers along with possible choices
    gloss = models.CharField(max_length = 1001, null=True, blank=True) # English translation for item. At the moment, we only have English instruments so definition and gloss are identical
    complexity_category = models.CharField(max_length = 101, null=True, blank=True) # category for complexity item. Currently blank.
    uni_lemma = models.CharField(max_length= 101, null=True, blank=True) # ID for matching terms across languages. Currently unused.
    item_order = models.IntegerField(validators=[MinValueValidator(1)])
    scoring_category = models.CharField(max_length = 101, null=True, blank=True) # used to provide scoring granulatity - uses item_type if blank
    def __unicode__(self):
        return "%s (%s, %s)" % (self.definition, self.instrument.verbose_name, self.itemID)
    def __str__(self):
        return f"%s (%s, %s)" % (self.definition, self.instrument.verbose_name, self.itemID)
    class Meta:
        unique_together = ('instrument', 'itemID') # Each instrument in the database must have a unique combination of instrument and itemID


#Model for storing demographic variables associated with a subject.
class BackgroundInfo(models.Model):
    administration = models.OneToOneField("researcher_UI.administration", on_delete=models.CASCADE) # Administration ID# unique to the entire database
    age = models.IntegerField(verbose_name = _("Age (in months)"), validators=[MinValueValidator(0)], default = 999) #age in months for child (views.py converts DOB field in forms.py into age for this model)
    sex = models.CharField(max_length = 1, blank=True, null=True, choices = (('M', _("Male")), ('F', _("Female")), ('O', _("Other")))) # Reported gender for child
    country = CountryField(verbose_name=_("Country"), blank = True, null=True)
    zip_code = models.CharField(max_length = 5, verbose_name = _('Zip Code (if you live in the U.S.)'), blank = True, null=True, validators=[RegexValidator(regex='^(\d{3}([*]{2})?)|([A-Z]{2})$', message=_('Please enter a valid U.S. zip code'))]) # Reported zip code for family. Follows Safe Harbor guidelines. Stores first 3 digits of zip code or state abbreviation.

    #Declared set of choices for birth order. Displays text version of integer ("First" instead of 1)
    birth_order_choices = [
        (1, _("1 (First)")),
        (2, _("2 (Second)")),
        (3, _("3 (Third)")),
        (4, _("4 (Fourth)")),
        (5, _("5 (Fifth)")),
        (6, _("6 (Sixth)")),
        (7, _("7 (Seventh)")),
        (8, _("8 (Eighth)")),
        (9, _("9 (Ninth)")),
        (10, _("10 or more (Tenth or Later)")),
        (0, _("Prefer not to disclose"))
    ]

    birth_order = models.IntegerField(verbose_name = _("Birth order"), choices = birth_order_choices, blank=True, null=True) # Birth order for child

    #Declared set of options for subjects born in a multiple birth
    multi_birth_choices = [
        (2, _("Twins")),
        (3, _("Triplets")),
        (4, _("Quadruplets")),
        (5, _("Quintuplets or greater")),
    ]

    multi_birth_boolean = models.IntegerField(verbose_name = _("Was your child born as part of a multiple birth?"), blank=True, null=True) # Boolean for multiple birth
    multi_birth = models.IntegerField(verbose_name = _("Twins, triplets, quadruplets, other?"), choices = multi_birth_choices, blank=True, null=True) # Elaboration on circumstances for subjects born in a multiple birth (twins, triplets, etc.)

    birth_weight_lb = models.FloatField(verbose_name = _("Birth weight"), blank=True, null=True) # Declared birthweight for subject (in lb and oz)
    birth_weight_kg = models.FloatField(verbose_name = _("Birth weight"), blank=True, null=True) # Declared birthweight for subject

    born_on_due_date = models.IntegerField(verbose_name = _("Was your child born earlier or later than their due date?"), blank=True, null=True) # Boolean for whether child was born on due date
    early_or_late = models.CharField(verbose_name = _("Was he/she early or late?"), max_length = 5, choices = (('early', _('Early')),('late', _('Late'))), blank=True, null=True) # Determines if child was born earlier or later than due date
    due_date_diff = models.IntegerField(verbose_name = _("By how many weeks? (round to the nearest week)"),blank=True, null=True, validators = [MinValueValidator(1, _("Number of weeks cannot be less than 1"))]) # Determines # of weeks between DOB and due date

    education_levels = [(x,str(x)) for x in range(5,25)] #Declares tuple of integers for # of years of education

    # Appends additional text descriptions for years of education w/ milestones (high school diploma, bachelor's degree, and master's degree)
    education_levels[12-5] = (12, _("12 (High school graduate)"))
    education_levels[16-5] = (16, _("16 (College graduate)"))
    education_levels[18-5] = (18, _("18 (Advanced degree)"))
    education_levels[23-5] = (23, _("23 or more"))
    education_levels[-1] = (0, _("Prefer not to disclose"))

    years = [(x,str(x)) for x in range(1950, datetime.date.today().year+2)] #Declares tuple for year of birth for parents/guardians
    years[-1] = (0, _("Prefer not to disclose"))

    caregiver_choices = (
        ('mother', _('Mother')),
        ('father',_('Father')),
        ('grandparent(s)', _('Grandparent(s)')),
        ('other',_('Other')),
    )
    
    primary_caregiver = models.CharField(verbose_name=_('Primary Caregiver'), choices=caregiver_choices, max_length=20, blank=True, null=True)
    primary_caregiver_other = models.CharField(max_length=25, null=True, blank=True)
    mother_yob = models.IntegerField(verbose_name = _("Primary Caregiver Year of birth"), choices=years, blank=True, null=True) # Asks for year of birth for mother. Can be used to roughly determine maternal age
    mother_education = models.IntegerField(verbose_name = _("Primary Caregiver Education"), help_text = _("Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)"), choices = education_levels, blank=True, null=True) # Asks for # of years of maternal education

    secondary_caregiver = models.CharField(verbose_name=_('Secondary Caregiver'), choices=caregiver_choices, max_length=20, null=True, blank=True)
    secondary_caregiver_other = models.CharField(max_length=25, null=True, blank=True)
    father_yob = models.IntegerField(verbose_name = _("Secondary Caregiver Year of birth"), choices = years, blank=True, null=True) # Asks for year of birth for father. Can be used to roughly determine paternal age
    father_education = models.IntegerField(verbose_name = _("Secondary Caregiver Education"), blank=True, null=True, help_text = _("Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)"), choices= education_levels) # Asks for # of years of paternal education

    annual_income = models.CharField(max_length = 30, verbose_name = _("Estimated Annual Family Income (in USD)"), blank=True, null=True) # Asks for bracket of annual income

    child_hispanic_latino = models.NullBooleanField(verbose_name = _("Is your child Hispanic or Latino?"), blank=True, null=True) # Asks whether child is hispanic/latino
    child_ethnicity = ArrayField(models.CharField(max_length = 1), blank=True, null=True) # Asks for child's ethnicity according to NIH ethnicity categories. Can check multiple answers.

    #Declares possible choices for child's family situation (# of caregivers, parents, grandparents, etc.)
    caregivers_choices = [
        (2, _("Two parents")), 
        (1, _("One parent")), 
        (3, _("One or both parents and other caregiver(s) (e.g., grandparent)")), 
        (4, _("Other caregivers (e.g., grandparent or grandparents)")), 
        (0, _("Prefer not to disclose")),
    ]

    caregiver_info = models.IntegerField(verbose_name = _("Who does your child live with?"), choices = caregivers_choices, blank=True, null=True) # Asks for child's family situation

    other_languages_boolean = models.IntegerField(blank = True, null=True) #Asks whether child is regularly exposed to other languages besides the instrument's language (currently English)
    other_languages = ArrayField(models.CharField(max_length = 101), blank = True, null=True) # Lists possible languages from languages.json that child may be exposed to
    language_from = models.CharField(max_length = 50, blank = True, verbose_name = _("From whom?"), null=True) # Free text response that asks who child hears other languages from
    language_days_per_week = models.IntegerField(null=True, blank = True, verbose_name = _("How many days per week is the child exposed to these languages?"), validators = [MaxValueValidator(7, _("Number of days per week cannot exceed 7")), MinValueValidator(1, _("Number of days per week cannot be less than 1"))], ) # Asks to quantify the # of days in a week that child is exposed to another language
    language_hours_per_day = models.IntegerField(null=True, blank = True, verbose_name = _("How many hours per day is the child exposed to these languages?"), validators = [MaxValueValidator(24, _("Number of hours per day cannot exceed 24")), MinValueValidator(1, _("Number of hours per day cannot be less than 1"))],) # Asks to quantify the # of hours a day that child is exposed to another language

    ear_infections_boolean = models.IntegerField(verbose_name = _("Has your child experienced chronic ear infections (5 or more)? "), blank=True, null=True) # Asks whether child has ever experiences 5+ ear infections
    ear_infections = models.CharField(max_length = 1001, null=True, blank = True, verbose_name = _("Has your child undergone interventions (e.g., tubes)?  Please describe")) # Free response describing treatment for chronic ear infections

    hearing_loss_boolean = models.IntegerField(verbose_name = _('Do you suspect that your child may have hearing loss?'), blank=True, null=True ) # Asks whether child is suspected to have hearing loss
    hearing_loss = models.CharField(max_length = 1001, blank = True, null=True,  verbose_name = _('Please describe') ) # Free response asking for elaboration on suspicion of hearing loss

    vision_problems_boolean = models.IntegerField(verbose_name = _('Is there some reason to suspect that your child may have vision problems?'), blank=True, null=True ) # Asks whether child is suspected to have vision problems
    vision_problems = models.CharField(max_length = 1001, blank = True, null=True, verbose_name = _('Please describe')) # Free response asking for elaboration on suspicion of vision problems

    illnesses_boolean = models.IntegerField(verbose_name = _('Has your child had any major illnesses, hospitalizations, or diagnosed disabilities?'), blank=True, null=True ) # Asks whether child has any major illnesses, diagnoses, or hospitalizations
    illnesses = models.CharField(max_length = 1001, blank = True, null=True, verbose_name = _("Please describe")) # Free response asking for elaboration on child's symptoms and diagnoses

    services_boolean = models.IntegerField(verbose_name = _('Has your child ever received any services for speech, language, or development issues?'), blank=True, null=True ) # Asks whether child has ever received therapy for speech or development
    services = models.CharField(max_length = 1001, blank = True, null=True, verbose_name = _("Please describe")) # Free response asking for elaboration on services received

    worried_boolean = models.IntegerField(verbose_name = _('Are you worried about your child\'s progress in language or communication?'), blank=True, null=True ) # Asks whether test-taker is worried about child's language acquisition
    worried = models.CharField(max_length = 1001, blank = True, null=True, verbose_name = _("Please describe")) # Free response asking for elaboration on test-taker's worries about child's language development

    learning_disability_boolean = models.IntegerField(verbose_name = _('Have you or anyone in your immediate family been diagnosed with a language or learning disability?'), blank=True, null=True ) # Asks whether a relative of the child has ever been diagnoses with a learning/language disability
    learning_disability = models.CharField(max_length = 1001, blank = True, null=True, verbose_name = _("Indicate which family member and provide a description")) # Free response asking for elaboration on the relationship between child and family member and a description of diagnosis

    form_filler_choices = [
        ('mother',_('Mother')),
        ('father',_('Father')),
        ('both parents', _('Both caregivers')),
        ('grandparent(s)', _('Grandparent(s)')),
        ('other',_('Other')),
    ]
    form_filler = models.CharField(verbose_name=_('Who is filling in the form?'), max_length=20, choices=form_filler_choices, blank=True, null=True)
    form_filler_other = models.CharField(max_length=25, blank=True, null=True)

#Model of zipcodes reported to be in 3-digit zip code prefixes with a population lower than 20,000. Tests with a zipcode found in this model will have their digits replaced with their state abbreviation.
class Zipcode(models.Model):
    zip_code=models.CharField(max_length = 5)
    zip_prefix=models.CharField(max_length = 3)
    population=models.IntegerField()
    state=models.CharField(max_length = 2)
