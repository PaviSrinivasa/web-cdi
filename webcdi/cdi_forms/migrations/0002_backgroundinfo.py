# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cdi_forms.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cdi_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(verbose_name=b'Age (in months)')),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birth_order', models.IntegerField(verbose_name=b'Birth order (enter number)', validators=[cdi_forms.models.validate_g_zero])),
                ('birth_weight', models.FloatField(verbose_name=b'Birth weight (In pounds)', validators=[cdi_forms.models.validate_g_zero])),
                ('born_on_due_date', models.BooleanField(verbose_name=b'Was your child born early or late?')),
                ('early_or_late', models.CharField(blank=True, max_length=5, null=True, verbose_name=b'Was he/she early or late?', choices=[(b'early', b'Early'), (b'late', b'Late')])),
                ('due_date_diff', models.IntegerField(blank=True, null=True, verbose_name=b'By how many weeks?', validators=[cdi_forms.models.validate_ne_zero])),
                ('mother_yob', models.IntegerField(verbose_name=b"Mother's (or Parent 1) Year of birth", choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('mother_education', models.IntegerField(help_text=b'Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)', verbose_name=b"Mother's (or Parent 1) Education", choices=[(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('father_yob', models.IntegerField(verbose_name=b"Father's (or Parent 2) Year of birth", choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('father_education', models.IntegerField(help_text=b'Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)', verbose_name=b"Father's (or Parent 2) Education", choices=[(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('annual_income', models.FloatField(verbose_name=b'Estimated Annual Family Income (in USD)', validators=[cdi_forms.models.validate_ge_zero])),
                ('child_hispanic_latino', models.NullBooleanField(verbose_name=b'Is your child Hispanic or Latino?')),
                ('child_ethnicity', models.CharField(max_length=101, null=True, blank=True)),
                ('caregiver_info', models.IntegerField(verbose_name=b'Does your child live with:', choices=[(2, b'Two parents'), (1, b'One parent'), (0, b'Other caregivers (e.g. grandparent)')])),
                ('other_languages_boolean', models.BooleanField()),
                ('other_languages', models.CharField(max_length=201, blank=True)),
                ('language_from', models.CharField(max_length=50, null=True, verbose_name=b'From Whom?', blank=True)),
                ('language_days_per_week', models.IntegerField(blank=True, null=True, verbose_name=b'How many days per week is the child exposed to these languages', validators=[django.core.validators.MaxValueValidator(7, b'Number of days per week cannot exceed 7'), django.core.validators.MinValueValidator(1, b'Number of days per week cannot be less than 1')])),
                ('language_hours_per_day', models.IntegerField(blank=True, null=True, verbose_name=b'How many hours per day is the child exposed to these languages', validators=[django.core.validators.MaxValueValidator(24, b'Number of hours per day cannot exceed 24'), django.core.validators.MinValueValidator(1, b'Number of hours per day cannot be less than 1')])),
                ('ear_infections_boolean', models.BooleanField(verbose_name=b'Has your child experienced chronic ear infections (5 or more)? ')),
                ('ear_infections', models.CharField(max_length=1001, null=True, verbose_name=b'Has your child undergone interventions (e.g., tubes)?  Please describe', blank=True)),
                ('hearing_loss_boolean', models.BooleanField(verbose_name=b'Do you suspect that your child may have hearing loss?')),
                ('hearing_loss', models.CharField(max_length=1001, null=True, verbose_name=b'Please describe', blank=True)),
                ('vision_problems_boolean', models.BooleanField(verbose_name=b'Is there some reason to suspect that your child may have vision problems?')),
                ('vision_problems', models.CharField(max_length=1001, null=True, verbose_name=b'Please describe', blank=True)),
                ('illnesses_boolean', models.BooleanField(verbose_name=b'Has your child had any major illnesses, hospitalizations, or diagnosed disabilities?')),
                ('illnesses', models.CharField(max_length=1001, null=True, verbose_name=b'Please describe', blank=True)),
                ('services_boolean', models.BooleanField(verbose_name=b'Has your child ever received any services for speech, language, or development issues?')),
                ('services', models.CharField(max_length=1001, null=True, verbose_name=b'Please describe', blank=True)),
                ('worried_boolean', models.BooleanField(verbose_name=b"Are you worried about your child's progress in language or communication?")),
                ('worried', models.CharField(max_length=1001, null=True, verbose_name=b'Please describe', blank=True)),
                ('learning_disability_boolean', models.BooleanField(verbose_name=b'Have you or anyone in your immediate family been diagnosed with a language or learning disability?')),
                ('learning_disability', models.CharField(max_length=1001, null=True, verbose_name=b'Indicate which family member and provide a description', blank=True)),
            ],
        ),
    ]