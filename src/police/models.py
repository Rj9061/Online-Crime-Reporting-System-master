from django.db import models
from django.contrib.auth.models import User


def image_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_images/%Y/%m/%d/', filename)

def video_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_audios/%Y/%m/%d/', filename)


designation_choice = (
    ('DGP', 'Director General of Police'),
    ('ADGP', 'Addl. Director General of Police'),
    ('IGP', 'Inspector General of Police'),
    ('DIGP', 'Deputy Inspector General of Police'),
    ('SPDCP', 'Superintendent of police Deputy Commissioner of Police(Selection Grade)'),
    ('SPDCPJ', 'Superintendent of police Deputy Commissioner of Police(Junior Management Grade)'),
    ('ASPADCP', 'Addl. Superintendent of police Addl.Deputy Commissioner of Police'),
    ('ASP', 'Assistant Superintendent of Police'),
    ('INSP', 'Inspector of Police'),
    ('SUB_INSP', 'Sub Inspector of Police.'),
    ('HVLDRM', 'Asst. Sub. Inspector/Havildar Major'),
    ('HVLDR', 'Havildar.'),
    ('LN', 'Lance Naik.'),
    ('CONS', 'Constable.'),
)


class Police(User):
    police_id = models.CharField(max_length=20)
    designation = models.CharField(max_length=10, choices=designation_choice, null=True)
    ward = models.ForeignKey('Ward', null=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Police'

    def __str__(self):
        return self.username


ward_choice = (
('GJ-01','Ahemdabad'),
('GJ-02','Mehsana'),
('GJ-03','Rajkot'),
('GJ-04','Bhavnagar'),
('GJ-05','Surat'),
('GJ-06','Vadodra'),
('GJ-07','Nadiad'),
('GJ-08','Palanpur'),
('GJ-09','Himmatnagar'),
('GJ-10','Jamnagar'),
('GJ-11','Junagadh'),
('GJ-12','Bhuj'),
('GJ-13','Surendranagar'),
('GJ-14','Amreli'),
('GJ-15','Valsad'),
('GJ-16','Bharuch'),
('GJ-17','Godhra'),
('GJ-18','Gandhinagar'),
('GJ-19','Bardoli'),
('GJ-20','Dahod'),
('GJ-21','Navsari'),
('GJ-22','Rajpipla'),
('GJ-23','Anand'),
('GJ-24','Patan'),
('GJ-25','Porbander'),
('GJ-26','Vyara'),
('GJ-27','Ahmedabad East'),
('GJ-28','Surat (Pal)'),
('GJ-29','Vadodara (Darjipura)'),
('GJ-30','Ahva-Dang'),
('GJ-31','Modasa (Arvali)'),
('GJ-32','Veraval (Gir-Somnath)'),
('GJ-33','Botad (Botad)'),
('GJ-34','Chhota Udepur (C.U)'),
('GJ-35','Lunawada (Mahisagar)'),
('GJ-36','Morbi (Morbi)'),
('GJ-37','Khambhaliya (D.B.Dwarka)'),
('GJ-38','Bavla (Ahmedabad)')
)




class Ward(models.Model):
    id = models.CharField(max_length=10, primary_key=True, choices=ward_choice)  # eg: RJ01w1,RJ01w2,RJ15w5
    address = models.CharField(max_length=255, blank=False)

    def get_contacts(self):
        contact_list = [i.contact for i in Ward.objects.get(id=self.id).contact_set]
        return contact_list

    def __str__(self):
        return self.id


class Contact(models.Model):
    ward = models.ForeignKey('ward')
    contact = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.ward






class Criminal(models.Model):
    name = models.CharField(max_length=255, blank=False)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField()
    caste = models.CharField(max_length=255)
    ward=models.ForeignKey(Ward,null=True)
    birth_mark_desc=models.TextField()
    height=models.CharField(max_length=255)
    complexion=models.CharField(max_length=255)
    eyes=models.CharField(max_length=255)

    def __str__(self):
        return self.name
