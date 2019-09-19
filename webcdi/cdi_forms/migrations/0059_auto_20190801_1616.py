# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-01 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdi_forms', '0058_auto_20190801_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundinfo',
            name='annual_income',
            field=models.CharField(blank=True, choices=[('<25000', 'Under $25,000'), ('25000-50000', '$25,000-$50,000'), ('50000-75000', '$50,000-$75,000'), ('75000-100000', '$75,000-$100,000'), ('100000-125000', '$100,000-$125,000'), ('125000-150000', '$125,000-$150,000'), ('150000-175000', '$150,000-$175,000'), ('175000-200000', '$175,000-$200,000'), ('>200000', 'Over $200,000'), ('Prefer not to disclose', 'Prefer not to disclose')], max_length=30, null=True, verbose_name='Estimated Annual Family Income (in USD)'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='birth_order',
            field=models.IntegerField(blank=True, choices=[(1, '1 (First)'), (2, '2 (Second)'), (3, '3 (Third)'), (4, '4 (Fourth)'), (5, '5 (Fifth)'), (6, '6 (Sixth)'), (7, '7 (Seventh)'), (8, '8 (Eighth)'), (9, '9 (Ninth)'), (10, '10 or more (Tenth or Later)'), (0, 'Prefer not to disclose')], null=True, verbose_name='Birth order'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='born_on_due_date',
            field=models.IntegerField(blank=True, null=True, verbose_name='Was your child born earlier or later than their due date?'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='caregiver_info',
            field=models.IntegerField(blank=True, choices=[(2, 'Two parents'), (1, 'One parent'), (3, 'One or both parents and other caregiver(s) (e.g., grandparent)'), (4, 'Other caregivers (e.g., grandparent or grandparents)'), (0, 'Prefer not to disclose')], null=True, verbose_name='Who does your child live with?'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='form_filler',
            field=models.CharField(blank=True, choices=[('mother', 'Mother'), ('father', 'Father'), ('both parents', 'Both caregivers'), ('grandparent(s)', 'Grandparent(s)'), ('other', 'Other')], max_length=20, null=True, verbose_name='Who is filling in the form?'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='mother_education',
            field=models.IntegerField(blank=True, choices=[(5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, '12 (High school graduate)'), (13, b'13'), (14, b'14'), (15, b'15'), (16, '16 (College graduate)'), (17, b'17'), (18, '18 (Advanced degree)'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, '23 or more'), (0, 'Prefer not to disclose')], help_text='Choose highest grade completed (12 = high school graduate; 16 = college graduate; 18 = advanced degree)', null=True, verbose_name='Primary Caregiver Education'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='mother_yob',
            field=models.IntegerField(blank=True, choices=[(1950, b'1950'), (1951, b'1951'), (1952, b'1952'), (1953, b'1953'), (1954, b'1954'), (1955, b'1955'), (1956, b'1956'), (1957, b'1957'), (1958, b'1958'), (1959, b'1959'), (1960, b'1960'), (1961, b'1961'), (1962, b'1962'), (1963, b'1963'), (1964, b'1964'), (1965, b'1965'), (1966, b'1966'), (1967, b'1967'), (1968, b'1968'), (1969, b'1969'), (1970, b'1970'), (1971, b'1971'), (1972, b'1972'), (1973, b'1973'), (1974, b'1974'), (1975, b'1975'), (1976, b'1976'), (1977, b'1977'), (1978, b'1978'), (1979, b'1979'), (1980, b'1980'), (1981, b'1981'), (1982, b'1982'), (1983, b'1983'), (1984, b'1984'), (1985, b'1985'), (1986, b'1986'), (1987, b'1987'), (1988, b'1988'), (1989, b'1989'), (1990, b'1990'), (1991, b'1991'), (1992, b'1992'), (1993, b'1993'), (1994, b'1994'), (1995, b'1995'), (1996, b'1996'), (1997, b'1997'), (1998, b'1998'), (1999, b'1999'), (2000, b'2000'), (2001, b'2001'), (2002, b'2002'), (2003, b'2003'), (2004, b'2004'), (2005, b'2005'), (2006, b'2006'), (2007, b'2007'), (2008, b'2008'), (2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015'), (2016, b'2016'), (2017, b'2017'), (2018, b'2018'), (2019, b'2019'), (0, 'Prefer not to disclose')], null=True, verbose_name='Primary Caregiver Year of birth'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='multi_birth_boolean',
            field=models.IntegerField(blank=True, null=True, verbose_name='Was your child born as part of a multiple birth?'),
        ),
        migrations.AlterField(
            model_name='backgroundinfo',
            name='primary_caregiver',
            field=models.CharField(blank=True, choices=[('mother', 'Mother'), ('father', 'Father'), ('grandparent(s)', 'Grandparent(s)'), ('other', 'Other')], max_length=20, null=True, verbose_name='Primary Caregiver'),
        ),
    ]
