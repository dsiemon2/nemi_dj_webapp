''' This module contain the model class defintions for the tables and views
that are used to implement the NEMI search pages. All tables and views are read
only and therefore have managed set to Fasle in each model's Meta data.
'''

from django.db import models

class MethodVWManager(models.Manager):
    
    def get_query_set(self):
        return super(MethodVWManager, self).get_query_set().exclude(method_subcategory_id=16)
    
class MethodVW(models.Model):
    
    method_id = models.IntegerField(primary_key=True)
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=2000, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    qc_requirements = models.CharField(max_length=2000, blank=True)
    cbr_only = models.CharField(max_length=1, blank=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    instrumentation_id = models.IntegerField()
    precision_descriptor_notes = models.CharField(max_length=3000, blank=True)
    screening = models.CharField(max_length=8, blank=True)
    rapidity = models.CharField(max_length=30, blank=True)
    waterbody_type = models.CharField(max_length=20, blank=True)
    matrix = models.CharField(max_length=12, blank=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_contact = models.CharField(max_length=450, blank=True)
    method_source_url = models.CharField(max_length=200, blank=True)
    method_subcategory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    method_subcategory = models.CharField(max_length=40)
    dl_type = models.CharField(max_length=11, blank=True)
    dl_type_description = models.CharField(max_length=50, blank=True)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    cost_effort_key = models.CharField(max_length=10, blank=True)
    instrumentation = models.CharField(max_length=20)
    instrumentation_description = models.CharField(max_length=200)
    regs_only = models.CharField(max_length=1)
    method_type_desc = models.CharField(max_length=100, blank=True)
    method_type_id = models.IntegerField()
    date_loaded = models.DateField(null=True)
    collected_sample_amt_ml = models.CharField(max_length=10, blank=True)
    collected_sample_amt_g = models.CharField(max_length=10, blank=True)
    liquid_sample_flag = models.CharField(max_length=1, blank=True)
    analysis_amt_ml = models.CharField(max_length=10, blank=True)
    analysis_amt_g = models.CharField(max_length=10, blank=True)
    ph_of_analytical_sample = models.CharField(max_length=10, blank=True)
    calc_waste_amt = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    quality_review_id = models.CharField(max_length=100, blank=True)
    pbt = models.CharField(max_length=1, blank=True)
    toxic = models.CharField(max_length=1, blank=True)
    corrosive = models.CharField(max_length=1, blank=True)
    waste = models.CharField(max_length=1, blank=True)
    assumptions_comments = models.CharField(max_length=2000, blank=True)
    
    objects = MethodVWManager()
    
    class Meta:
        db_table = u'method_vw'
        managed = False
                
class MethodSummaryVW(models.Model):
    
    revision_id = models.IntegerField()
    revision_information = models.CharField(max_length=100)
    revision_flag = models.IntegerField(null=True)
    mimetype = models.CharField(max_length=50, blank=True)
#    mydoc -- Unused
#    method_pdf -- Unused
    pdf_size  = models.IntegerField(null=True)
    method_id = models.IntegerField(primary_key=True) 
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=2000, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    method_source_contact = models.CharField(max_length=450, blank=True)
    qc_requirements = models.CharField(max_length=2000, blank=True)
    waterbody_type = models.CharField(max_length=20, blank=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_url = models.CharField(max_length=200, blank=True)
    precision_descriptor_notes = models.CharField(max_length=3000, blank=True)
    method_subcategory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    method_subcategory = models.CharField(max_length=40)
    method_type_desc = models.CharField(max_length=100, blank=True)
    dl_type = models.CharField(max_length=11, blank=True)
    dl_type_description = models.CharField(max_length=50, blank=True)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    pdf_name = models.CharField(max_length=34, blank=True)
    pdf_name2 = models.CharField(max_length=44, blank=True)
    collected_sample_amt_ml = models.CharField(max_length=10, blank=True)
    collected_sample_amt_g = models.CharField(max_length=10, blank=True)
    liquid_sample_flag = models.CharField(max_length=1, blank=True)
    analysis_amt_ml = models.CharField(max_length=10, blank=True)
    analysis_amt_g = models.CharField(max_length=10, blank=True)
    ph_of_analytical_sample = models.CharField(max_length=10, blank=True)
    calc_waste_amt = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    quality_review_id = models.CharField(max_length=100, blank=True)
    pbt = models.CharField(max_length=1, blank=True)
    toxic = models.CharField(max_length=1, blank=True)
    corrosive = models.CharField(max_length=1, blank=True)
    waste = models.CharField(max_length=1, blank=True)
    assumptions_comments = models.CharField(max_length=2000, blank=True)
     
    class Meta:
        db_table = u'method_summary_vw'
        managed = False
        
class MethodAnalyteVW(models.Model):
     
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_url = models.CharField(max_length=200, blank=True)
    method_subcateory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    method_subcategory = models.CharField(max_length=40)
    dl_type = models.CharField(max_length=11)
    dl_type_description = models.CharField(max_length=50)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    matrix = models.CharField(max_length=12, blank=True)
    dl_units = models.CharField(max_length=20)
    dl_value = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_dl_value = models.CharField(max_length=40, blank=True)
    analyte_method_id = models.IntegerField(primary_key=True)
    analyte_id = models.IntegerField()
    accuracy = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_accuracy = models.CharField(max_length=40, blank=True)
    accuracy_order = models.IntegerField(null=True)
    accuracy_units = models.CharField(max_length=40, blank=True)
    precision = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_precision = models.CharField(max_length=40, blank=True)
    precision_units= models.CharField(max_length=30, blank=True)
    prec_acc_conc_used = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    false_positive_value = models.IntegerField(null=True)
    false_negative_value = models.IntegerField(null=True)
    analyte_code = models.CharField(max_length=20, blank=True)
    analyte_name = models.CharField(max_length=240, blank=True)
    preferred = models.IntegerField(null=True)
    analyte_cbr = models.CharField(max_length=1, blank=True)
    dl_units_description = models.CharField(max_length=60, blank=True)
    precision_units_description = models.CharField(max_length=100, blank=True)
    accuracy_units_description = models.CharField(max_length=50, blank=True)
    method_id = models.IntegerField(null=True)
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=2000, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    cbr_only = models.CharField(max_length=1, blank=True)
    qc_requirements = models.CharField(max_length=2000, blank=True)
    instrumentation_id = models.IntegerField()
    instrumentation = models.CharField(max_length=20)
    instrumentation_description = models.CharField(max_length=200)
    precision_descriptor_notes = models.CharField(max_length=3000, blank=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    
    class Meta:
        db_table = u'method_analyte_vw'
        managed = False
        
class AnalyteCodeRel(models.Model):
    
    analyte_code = models.CharField(max_length=20)
    analyte_name = models.CharField(max_length=240, primary_key=True)
    preferred = models.IntegerField(null=True)
    changed = models.DateField()
    data_entry = models.CharField(max_length=20, blank=True)
    analyte_type = models.CharField(max_length=50, blank=True)
    
    class Meta:
        db_table = u'analyte_code_rel'
        managed = False

class MethodAnalyteAllVW(models.Model):
    
    analysis_amt_g = models.CharField(max_length=10, blank=True)
    ph_of_analytical_sample = models.CharField(max_length=10, blank=True)
    calc_waste_amt = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    quality_review_id = models.CharField(max_length=100, blank=True)
    pbt = models.CharField(max_length=1, blank=True)
    toxic = models.CharField(max_length=1, blank=True)
    corrosive = models.CharField(max_length=1, blank=True)
    waste = models.CharField(max_length=1, blank=True)
    assumptions_comments = models.CharField(max_length=2000, blank=True)
    method_type_desc = models.CharField(max_length=100, blank=True)
    prec_acc_conc_used = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    false_positive_value = models.IntegerField(null=True)
    false_negative_value = models.IntegerField(null=True)
    dl_units_description = models.CharField(max_length=60, blank=True)
    precision_units_description = models.CharField(max_length=100, blank=True)
    accuracy_units_description = models.CharField(max_length=50, blank=True)
    instrumentation = models.CharField(max_length=20)
    instrumentation_description = models.CharField(max_length=200)
    analyte_code = models.CharField(max_length=20)
    analyte_name = models.CharField(max_length=240)
    preferred = models.IntegerField(null=True)
    usgs_pcode = models.CharField(max_length=6, blank=True)
    analyte_cbr = models.CharField(max_length=1, blank=True)
    analyte_type = models.CharField(max_length=50, blank=True)
    method_id = models.IntegerField()
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=2000, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    cbr_only = models.CharField(max_length=1, blank=True)
    qc_requirements = models.CharField(max_length=2000, blank=True)
    instrumentation_id = models.IntegerField(null=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    waterbody_type = models.CharField(max_length=20, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_url = models.CharField(max_length=200, blank=True)
    method_source_contact = models.CharField(max_length=450, blank=True)
    precision_descriptor_notes = models.CharField(max_length=3000, blank=True)
    method_subcategory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    method_subcategory = models.CharField(max_length=40)
    dl_type = models.CharField(max_length=11, blank=True)
    dl_type_description = models.CharField(max_length=50, blank=True)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    cost_effort_key = models.CharField(max_length=10, blank=True)
    matrix = models.CharField(max_length=12, blank=True)
    collected_sample_amt_ml = models.CharField(max_length=10, blank=True)
    collected_sample_amt_g = models.CharField(max_length=10, blank=True)
    liquid_sample_flag = models.CharField(max_length=1, blank=True)
    analysis_amt_ml = models.CharField(max_length=10, blank=True)
    dl_units = models.CharField(max_length=20)
    dl_value = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_dl_value = models.CharField(max_length=40, blank=True)
    analyte_method_id = models.IntegerField(primary_key=True)
    analyte_id = models.IntegerField()
    accuracy = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_accuracy = models.CharField(max_length=40, blank=True)
    accuracy_order = models.IntegerField(null=True)
    accuracy_units = models.CharField(max_length=40, blank=True)
    precision = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_precision = models.CharField(max_length=40, blank=True)
    precision_units = models.CharField(max_length=30, blank=True)
    
    class Meta:
        db_table = 'method_analyte_all_vw'
        managed = False
        
class AnalyteCodeVW(models.Model):
    
    analyte_analyte_id = models.IntegerField(primary_key=True)
    analyte_analyte_code = models.CharField(max_length=20)
    ac_analyte_code = models.CharField(max_length=20, blank=True)
    ac_analyte_name = models.CharField(max_length=240, blank=True)
    ac_preferred = models.IntegerField(null=True)
    ac_analyte_type = models.CharField(max_length=50, blank=True)
    
    class Meta:
        db_table = 'analyte_code_vw'
        managed = False
        
        
class MethodAnalyteJnStgVW(models.Model):
    
    matrix = models.CharField(max_length=12, blank=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_contact = models.CharField(max_length=450, blank=True)
    waterbody_type = models.CharField(max_length=20, blank=True)
    method_source_url = models.CharField(max_length=200, blank=True)
    technique = models.CharField(max_length=50, blank=True)
    method_subcategory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    dl_type = models.CharField(max_length=11, blank=True)
    dl_type_description = models.CharField(max_length=50, blank=True)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    cost_effort_key = models.CharField(max_length=10, blank=True)
    dl_units = models.CharField(max_length=20, blank=True)
    dl_value = models.DecimalField(max_digits=21, decimal_places=6, blank=True)
    analyte_method_id = models.IntegerField(null=True)
    precision = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    analyte_id = models.IntegerField(null=True)
    accuracy = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    accuracy_units = models.CharField(max_length=40, blank=True)
    approved = models.CharField(max_length=1)
    precision_units = models.CharField(max_length=30, blank=True)
    prec_acc_conc_used = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    false_positive_value = models.IntegerField(null=True)
    false_negative_value = models.IntegerField(null=True)
    analyte_code = models.CharField(max_length=20, blank=True)
    analyte_name = models.CharField(max_length=240, blank=True)
    preferred = models.IntegerField(null=True)
    analyte_type = models.CharField(max_length=50, blank=True)
    dl_units_description = models.CharField(max_length=60, blank=True)
    precision_units_description = models.CharField(max_length=100, blank=True)
    accuracy_units_description = models.CharField(max_length=50, blank=True)
    method_id = models.IntegerField(primary_key=True)
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=2000, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    rapidity = models.CharField(max_length=30, blank=True)
    qc_requirements = models.CharField(max_length=2000, blank=True)
    instrumentation_id = models.IntegerField()
    instrumentation = models.CharField(max_length=20)
    instrumentation_description = models.CharField(max_length=200)
    precision_descriptor_notes = models.CharField(max_length=3000, blank=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'method_analyte_jn_stg_vw'
        managed = False
        
class MethodStgSummaryVw(models.Model):
    
    revision_id = models.IntegerField()
    revision_information = models.CharField(max_length=100)
    revision_flag = models.IntegerField(null=True)
    method_id = models.IntegerField(primary_key=True)
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=2000, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    method_source_contact = models.CharField(max_length=450, blank=True)
    qc_requirements = models.CharField(max_length=2000, blank=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_url = models.CharField(max_length=200, blank=True)
    precision_descriptor_notes = models.CharField(max_length=3000, blank=True)
    method_subcategory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    method_subcategory = models.CharField(max_length=40)
    dl_type = models.CharField(max_length=11, blank=True)
    dl_type_description = models.CharField(max_length=50, blank=True)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    method_type_desc = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table = 'method_stg_summary_vw'
        managed = False
        
class RegulationRef(models.Model):
    regulation_id = models.IntegerField(primary_key=True)
    regulation = models.CharField(max_length=10)
    regulation_name = models.CharField(max_length=60)
    reg_location = models.CharField(max_length=30)
    reg_location_2 = models.CharField(max_length=30, blank=True)
    
    class Meta:
        db_table = 'regulation_ref'
        managed = False
        
class RegQueryVW(models.Model):
    
    conc_range_units = models.CharField(max_length=20, blank=True)
    interferences = models.CharField(max_length=3000, blank=True)
    analyte_method_id = models.IntegerField()
    qc_requirements = models.CharField(max_length=2000, blank=True)
    false_positive_value = models.IntegerField(null=True)
    false_negative_value = models.IntegerField(null=True)
    link_to_full_method = models.CharField(max_length=240, blank=True)
    sample_handling = models.CharField(max_length=3000, blank=True)
    max_holding_time = models.CharField(max_length=300, blank=True)
    sample_prep_methods = models.CharField(max_length=100, blank=True)
    relative_cost_id = models.IntegerField(null=True)
    method_source = models.CharField(max_length=20)
    method_source_name = models.CharField(max_length=150)
    method_source_url = models.CharField(max_length=200, blank=True)
    method_subcategory_id = models.IntegerField()
    method_category = models.CharField(max_length=50)
    method_subcategory = models.CharField(max_length=40)
    dl_type = models.CharField(max_length=11, blank=True)
    dl_type_description = models.CharField(max_length=50, blank=True)
    source_citation_name = models.CharField(max_length=450, blank=True)
    source_citation = models.CharField(max_length=30)
    source_citation_information = models.CharField(max_length=1500, blank=True)
    relative_cost_symbol = models.CharField(max_length=7, blank=True)
    relative_cost = models.CharField(max_length=40, blank=True)
    revision_id = models.IntegerField(primary_key=True)
    revision_information = models.CharField(max_length=100)
    revision_flag = models.IntegerField(blank=True)
    mimetype = models.CharField(max_length=50, blank=True)
    #mydoc
    regulation_name = models.CharField(max_length=60)
    regulation = models.CharField(max_length=10)
    reg_location = models.CharField(max_length=30)
    reg_location_2 = models.CharField(max_length=30, blank=True)
    regulation_note = models.CharField(max_length=200, blank=True)
    analyte_revision_id = models.IntegerField()
    dl_units = models.CharField(max_length=20)
    dl_value = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_dl_value = models.CharField(max_length=40, blank=True)
    instrumentation_id = models.IntegerField()
    analyte_id = models.IntegerField()
    accuracy = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_accuracy = models.CharField(max_length=40, blank=True)
    accuracy_order = models.IntegerField(null=True)
    accuracy_units = models.CharField(max_length=40, blank=True)
    precision = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    sub_precision = models.CharField(max_length=40, blank=True)
    precision_units = models.CharField(max_length=30, blank=True)
    precision_descriptor_notes = models.CharField(max_length=300, blank=True)
    prec_acc_conc_used = models.DecimalField(max_digits=21, decimal_places=6, null=True)
    instrumentation = models.CharField(max_length=20)
    instrumentation_description = models.CharField(max_length=200)
    analyte_code = models.CharField(max_length=20)
    analyte_name = models.CharField(max_length=240)
    preferred = models.IntegerField(null=True)
    method_id = models.IntegerField()
    source_method_identifier = models.CharField(max_length=30)
    method_descriptive_name = models.CharField(max_length=250)
    method_official_name = models.CharField(max_length=250)
    method_source_id = models.IntegerField()
    source_citation_id = models.IntegerField()
    dl_units_description = models.CharField(max_length=60, blank=True)
    precision_units_description = models.CharField(max_length=100, blank=True)
    accuracy_units_description = models.CharField(max_length=50, blank=True)
    brief_method_summary = models.CharField(max_length=4000)
    scope_and_application = models.CharField(max_length=200, blank=True)
    media_name = models.CharField(max_length=30)
    dl_type_id = models.IntegerField(null=True)
    dl_note = models.CharField(max_length=2000, blank=True)
    applicable_conc_range = models.CharField(max_length=300, blank=True)
    
    class Meta:
        db_table = 'reg_query_vw'
        managed = False
        
class RegulatoryMethodReport(models.Model):
    
    analyte_name = models.CharField(max_length=240, primary_key=True)
    epa_id = models.IntegerField(null=True)
    epa_rev_id = models.IntegerField(null=True)
    epa = models.CharField(max_length=143, blank=True)
    standard_methods_id = models.IntegerField(null=True)
    standard_methods_rev_id = models.IntegerField(null=True)
    standard_methods = models.CharField(max_length=143, blank=True)
    usgs_id = models.IntegerField(null=True)
    usgs_rev_id = models.IntegerField(null=True)
    usgs = models.CharField(max_length=143, blank=True)
    astm_id = models.IntegerField(null=True)
    astm_rev_id = models.IntegerField(null=True)
    astm = models.CharField(max_length=143, blank=True)
    other_id = models.IntegerField(null=True)
    other_rev_id = models.IntegerField(null=True)
    other = models.CharField(max_length=143, blank=True)
    
    class Meta:
        db_table = 'regulatory_method_report'
        managed = False
        
