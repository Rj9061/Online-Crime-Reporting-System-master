from django import forms
from .models import Case

# ward_choice = (
# ('GJ-01','Ahemdabad'),
# ('GJ-02','Mehsana'),
# ('GJ-03','Rajkot'),
# ('GJ-04','Bhavnagar'),
# ('GJ-05','Surat'),
# ('GJ-06','Vadodra'),
# ('GJ-07','Nadiad'),
# ('GJ-08','Palanpur'),
# ('GJ-09','Himmatnagar'),
# ('GJ-10','Jamnagar'),
# ('GJ-11','Junagadh'),
# ('GJ-12','Bhuj'),
# ('GJ-13','Surendranagar'),
# ('GJ-14','Amreli'),
# ('GJ-15','Valsad'),
# ('GJ-16','Bharuch'),
# ('GJ-17','Godhra'),
# ('GJ-18','Gandhinagar'),
# ('GJ-19','Bardoli'),
# ('GJ-20','Dahod'),
# ('GJ-21','Navsari'),
# ('GJ-22','Rajpipla'),
# ('GJ-23','Anand'),
# ('GJ-24','Patan'),
# ('GJ-25','Porbander'),
# ('GJ-26','Vyara'),
# ('GJ-27','Ahmedabad East'),
# ('GJ-28','Surat (Pal)'),
# ('GJ-29','Vadodara (Darjipura)'),
# ('GJ-30','Ahva-Dang'),
# ('GJ-31','Modasa (Arvali)'),
# ('GJ-32','Veraval (Gir-Somnath)'),
# ('GJ-33','Botad (Botad)'),
# ('GJ-34','Chhota Udepur (C.U)'),
# ('GJ-35','Lunawada (Mahisagar)'),
# ('GJ-36','Morbi (Morbi)'),
# ('GJ-37','Khambhaliya (D.B.Dwarka)'),
# ('GJ-38','Bavla (Ahmedabad)')
# )




class case_form(forms.ModelForm):
    # ward_id=forms.ChoiceField(ward_choice)
    incident_time=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Case
        fields="__all__"
        exclude = ['cyber_case_categories','approved','updated','timestamp','solved']

    def __init__(self, *args, **kwargs):
        super(case_form, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            "name":"title"})
        self.fields['case_categories'].widget.attrs.update({
            'class': 'form-control',
            "name":"case_categories"})

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            "name":"description"})
        self.fields['reg_from_loc'].widget.attrs.update({
            'class': 'form-control',
            "name":"reg_from_loc"})
        self.fields['ward_id'].widget.attrs.update({
            'class': 'form-control',
            "name":"ward_id"})
        self.fields['incident_time'].widget.attrs.update({
            'class': 'form-control',
            "name":"incident_time"})



class cyber_case_form(forms.ModelForm):
    # ward_id=forms.ChoiceField(ward_choice)
    incident_time=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Case
        fields="__all__"
        exclude = ['case_categories','approved','updated','timestamp','solved']

    def __init__(self, *args, **kwargs):
        super(cyber_case_form, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            "name":"title"})
        self.fields['cyber_case_categories'].widget.attrs.update({
            'class': 'form-control',
            "name":"case_categories"})

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            "name":"description"})
        self.fields['reg_from_loc'].widget.attrs.update({
            'class': 'form-control',
            "name":"reg_from_loc"})
        self.fields['ward_id'].widget.attrs.update({
            'class': 'form-control',
            "name":"ward_id"})
        self.fields['incident_time'].widget.attrs.update({
            'class': 'form-control',
            "name":"incident_time"})
















    # title = models.CharField(max_length=80, blank=False)
    # case_categories = models.ForeignKey(CaseCategory,null=True,blank=True)
    # cyber_case_categories = models.ForeignKey(CyberCaseCategories,null=True,blank=True)
    # description = models.TextField()
    # reg_from_loc = models.CharField(max_length=255, blank=False)
    # userid = models.ForeignKey(Citizen)
    # ward_id = models.CharField(max_length=255, blank=False)
    # incident_time = models.DateTimeField()
    # approved=models.BooleanField()
    # solved=models.BooleanField()
    
    # timestamp = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)