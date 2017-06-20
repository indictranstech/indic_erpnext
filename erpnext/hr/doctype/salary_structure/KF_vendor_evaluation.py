class DocType:
  def __init__(self, doc, doclist =[]):
    self.doc = doc
    self.doclist = doclist
    self.prefix = is_testing and 'test' or 'tab'

#----autonaming of document		
  def autoname(self):
    self.doc.name = make_autoname('VE/' + cstr(self.doc.site_id)[5:] + '/.######')

#----pulling vendor details when trigger vendor_name-----
  def get_vendor_det(self):
    vd = sql("select name from `tabVendor` where vendor_name = '%s' " % (self.doc.vendor_name))
    ret = {
      'vendor_id' : vd[0][0] or ''
    }
    return cstr(ret)
    
#----pulling vendor details--------		
  def get_vendor(self):
    vendor = Document('Vendor', self.doc.vendor_id)
    ret = {
      'vendor_name' : vendor.vendor_name or ''
    }
    return str(ret)

#-------Pulling site detail from site master----------
#--------------------------------------------------------    
  def get_site_detail(self):
    site = Document('Site', self.doc.site_id)
    ret = {
      'site_name' : site.site_name or '',
      'client_id' : site.client_id or '',
      'client_name' : site.client_name or '',
      'region' : site.region or '',
      'kf_branch' : site.kf_branch or '',
      'location' : site.location or ''
    }
    return cstr(ret)    

#------ autogenerating of HK -----    
  def get_hk_detail(self):
    desc = [['Floor Cleaning','1'],['Washroom Cleaning','1'],['Workstation cleaning','1'],['Carpet care & maintenance','1'],['Cleaning & maintenance of Furniture & Upholstery','1'],['Utility area cleaning','1'],['Internal glass cleaning','1'],['Common area/ premises cleaning','1'],['House Keeping Total','0']]
    if not getlist(self.doclist, 've_details1'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details1', 'VE Detail1',1,self.doclist)
        od.description = d[0]
        od.rating1=d[1]
	idx = idx + 1

#------ autogenerating of bt -----    
  def get_bt_detail(self):
    desc = [['Technical knowledge','1'],['Practical knowledge of equipment','1'],['Operation of equipment','1'],['Care & maintenance of equipment','1'],['Understanding & grasping of the work at site','1'],['Following systems & procedures (Handing over of shift duties, Safety, Maint procedures etc.)','1'],['Documentation and maintenance of reports and records','1'],['Technical Total','0']]
    if not getlist(self.doclist, 've_details2'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details2', 'VE Detail2',1,self.doclist)
        od.description = d[0]
        od.rating2=d[1]
	idx = idx + 1

#------ autogenerating of cp -----    
  def get_cp_detail(self):
    desc = [['Manners & etiquette of staff','1'],['Service in a conference / meeting / board rooms','1'],['Maintenance of Cutlery, Crockery & Glassware','1'],['Maintenance of Pantry Area','1'],['Maintenance of Vending Machine/ Equipment','1'],['Ability to communicate','1'],['Pantry Services Total','0']]
    if not getlist(self.doclist, 've_details3'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details3', 'VE Detail3',1,self.doclist)
        od.description = d[0]
        od.rating3=d[1]
	idx = idx + 1
 
#------ autogenerating of dh -----    
  def get_dh_detail(self):
    desc = [['Maintenance of plants - Watering,Trimming','1'],['Maintenance of lawns - Watering, Mowing & Maintenance','1'],['Maintenance of plotted plants - Watering, Rotation, Trimming & Nourishment','1'],['Maintainince of Gardening tools, Equipment & Sprinklers','1'],['Overall maintenance of Landscape design','1'],['Proper supply & effective use of fertilisers & insecticides','1'],['Horiculture Total','0']]
    if not getlist(self.doclist, 've_details4'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details4', 'VE Detail4',1,self.doclist)
        od.description = d[0]
        od.rating4=d[1]
	idx = idx + 1
 
#------ autogenerating of es -----    
  def get_es_detail(self):
    desc = [['Alertness of guards','1'],['Interaction with client/visitors/vendors','1'],['Training to security staff','1'],['Night rounds by security field officers','1'],['Documentation','1'],['Handing over when changing shifts','1'],['Awareness of security and Fire Fighting systems at site','1'],['Security Total','0']]
    if not getlist(self.doclist, 've_details5'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details5', 'VE Detail5',1,self.doclist)
        od.description = d[0]
        od.rating5=d[1]
	idx = idx + 1

#------ autogenerating of fg -----    
  def get_fg_detail(self):
    desc = [['Legal compliance','1'],['Briefing / Debriefing and grooming','1'],['Attendence, Deployment and replacement','1'],['Day to day Operations and Work methods','1'],['Equipments, Tools and Tackles','1'],['Honesty and Integrity','1'],['Grooming & etiquette of staff','1'],['Standard of Uniforms','1'],['Reward & Recognition','1'],['On time invoice submission','1'],['Training imparted to staff','1'],['Proactivness displayed by staff','1'],['Police verification document submission','1'],['Response time of vendor','1'],['Staff attrition','1'],['Supervisory skills of staff','1'],['General Total','0']]
    if not getlist(self.doclist, 've_details6'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details6', 'VE Detail6',1,self.doclist)
        od.description = d[0]
        od.rating6=d[1]
	idx = idx + 1


#------ autogenerating of ga -----    
  def get_ga_detail(self):
    desc = [['Conduct of visits as per AMC','1'],['Skill of staff providing services','1'],['Response to calls for attending breakdowns or others issues','1'],['Organising work at site','1'],['Observing safety at site','1'],['Following rules/regulations of client/KF at site','1'],['Submission of service reports','1'],['AMC vendors Total','0']]
    if not getlist(self.doclist, 've_details7'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details7', 'VE Detail7',1,self.doclist)
        od.description = d[0]
        od.rating7=d[1]
	idx = idx + 1

#------autogenerating of evaluation table------    
  def get_eval_detail(self):
    if not self.doc.evaluator_name:
      self.doc.evaluator_name = session['user']
      
    desc = ['A House keeping','B Technical','C Pantry Services','D Horiculture','E Security','F General','G AMC vendors','Total','Average','Percentage']
    if not getlist(self.doclist, 've_details'):
      idx = 0
      for d in desc:
        od = addchild(self.doc, 've_details', 'VE Detail',1,self.doclist)
        od.description = d
	idx = idx + 1
 

#----validations-------
  def validate(self):
    if getdate(self.doc.evaluation_date) > getdate(nowdate()):
      msgprint('Evaluation Date cannot be a Future Date')
      raise Exception
    if (self.doc.fg!=1):
      msgprint('General Section is Mandatory for every vendor.')
      raise Exception
    if not self.doc.vcode:
        import random
        self.doc.vcode=''.join(random.choice('0123456789ABCDEF') for i in range(16))

    if not self.doc.appointment_letter or not self.doc.employment_cards or not self.doc.wage_slips or not self.doc.register_of_wages or not self.doc.muster_roll or not self.doc.sal_pay_proof or not self.doc.register_wages_of_kf_fm or not self.doc.leave_wage_register or not self.doc.register_of_workmen or not self.doc.register_of_deductions or not self.doc.register_of_fines or not self.doc.register_of_advances or not self.doc.register_of_overtime or not self.doc.deposit_summary_esi_pf or not self.doc.pf_challan or not self.doc.pf_ecr or not self.doc.pf_remittance_confirmation_slips or not self.doc.esi_challan or not self.doc.copy_esi_card or not self.doc.emp_monthly_contibution_history or not self.doc.pf_esi_monthly_summary or not self.doc.equal_remmuneration or not self.doc.maternity_register or not self.doc.service_certificate :
         self.doc.vendor_points,self.doc.vendor_percentage,self.doc.standard_percentage,self.doc.overall_performance=0 ,0,0,'Needs Replacement'
         #msgprint("set 0 score")
    self.doc.email_link='<a href="http://fms.kfcommunity.com/fms/images/logos/acknowledgement.html?vid='+self.doc.name+'&code='+cstr(self.doc.vcode)+'"><b>Click Here to Acknowledgement ..!</b></a>'
    

  #----calculations-------  gangadhar--	
  def on_update(self):
    at=bt1=ct=dt=et=ft=gt=tot=count=avg=per=0
    if (self.doc.hk==1):
      for d in getlist(self.doclist, 've_details1'):
        if d.description=='Floor Cleaning':
          at=at+int(d.rating1)
        if d.description=='Washroom Cleaning':
          at=at+int(d.rating1)
        if d.description=='Workstation cleaning':
          at=at+int(d.rating1)
        if d.description=='Carpet care & maintenance':
          at=at+int(d.rating1)
        if d.description=='Cleaning & maintenance of Furniture & Upholstery':
          at=at+int(d.rating1)
        if d.description=='Utility area cleaning':
          at=at+int(d.rating1)
        if d.description=='Internal glass cleaning':
          at=at+int(d.rating1)
        if d.description=='Common area/ premises cleaning':
          at=at+int(d.rating1)
        if d.description=='House Keeping Total':
          d.rating1=at
      count=count+8
      msgprint(count)
    if (self.doc.bt==1):
      for d in getlist(self.doclist, 've_details2'):
        if d.description=='Technical knowledge':
          bt1=bt1+int(d.rating2)
        if d.description=='Practical knowledge of equipment':
          bt1=bt1+int(d.rating2)
        if d.description=='Operation of equipment':
          bt1=bt1+int(d.rating2)
        if d.description=='Care & maintenance of equipment':
          bt1=bt1+int(d.rating2)
        if d.description=='Cleaning & maintenance of Furniture & Upholstery':
          bt1=bt1+int(d.rating2)
        if d.description=='Understanding & grasping of the work at site':
          bt1=bt1+int(d.rating2)
        if d.description=='Following systems & procedures (Handing over of shift duties, Safety, Maint procedures etc.)':
          bt1=bt1+int(d.rating2)
        if d.description=='Documentation and maintenance of reports and records':
          bt1=bt1+int(d.rating2)
        if d.description=='Technical Total':
          d.rating2=bt1
      count=count+7   
      #msgprint(count)
    if (self.doc.cp==1):
      for d in getlist(self.doclist, 've_details3'):
        if d.description=='Manners & etiquette of staff':
          ct=ct+int(d.rating3)
        if d.description=='Service in a conference / meeting / board rooms':
          ct=ct+int(d.rating3)
        if d.description=='Maintenance of Cutlery, Crockery & Glassware':
          ct=ct+int(d.rating3)
        if d.description=='Maintenance of Pantry Area':
          ct=ct+int(d.rating3)
        if d.description=='Maintenance of Vending Machine/ Equipment':
          ct=ct+int(d.rating3)
        if d.description=='Ability to communicate':
          ct=ct+int(d.rating3)
        if d.description=='Pantry Services Total':
          d.rating3=ct
      count=count+6    
      #msgprint(count)
    if (self.doc.dh==1):
      for d in getlist(self.doclist, 've_details4'):
        if d.description=='Maintenance of plants - Watering,Trimming':
          dt=dt+int(d.rating4)
        if d.description=='Maintenance of lawns - Watering, Mowing & Maintenance':
          dt=dt+int(d.rating4)
        if d.description=='Maintenance of plotted plants - Watering, Rotation, Trimming & Nourishment':
          dt=dt+int(d.rating4)
        if d.description=='Maintainince of Gardening tools, Equipment & Sprinklers':
          dt=dt+int(d.rating4)
        if d.description=='Overall maintenance of Landscape design':
          dt=dt+int(d.rating4)
        if d.description=='Proper supply & effective use of fertilisers & insecticides':
          dt=dt+int(d.rating4)
        if d.description=='Horiculture Total':
          d.rating4=dt
      count=count+6    
      #msgprint(count)
    if (self.doc.es==1):
      for d in getlist(self.doclist, 've_details5'):
        if d.description=='Alertness of guards':
          et=et+int(d.rating5)
        if d.description=='Interaction with client/visitors/vendors':
          et=et+int(d.rating5)
        if d.description=='Training to security staff':
          et=et+int(d.rating5)
        if d.description=='Night rounds by security field officers':
          et=et+int(d.rating5)
        if d.description=='Documentation':
          et=et+int(d.rating5)
        if d.description=='Handing over when changing shifts':
          et=et+int(d.rating5)
        if d.description=='Awareness of security and Fire Fighting systems at site':
          et=et+int(d.rating5)
        if d.description=='Security Total':
          d.rating5=et
      count=count+7
      #msgprint(count)
    
    if (self.doc.fg==1):
      for d in getlist(self.doclist, 've_details6'):
        if d.description=='Legal compliance':
          ft=ft+int(d.rating6)
        if d.description=='Briefing / Debriefing and grooming':
          ft=ft+int(d.rating6)
        if d.description=='Attendence, Deployment and replacement':
          ft=ft+int(d.rating6)
        if d.description=='Day to day Operations and Work methods':
          ft=ft+int(d.rating6)
        if d.description=='Equipments, Tools and Tackles':
          ft=ft+int(d.rating6)
        if d.description=='Grooming & etiquette of staff':
          ft=ft+int(d.rating6)
        if d.description=='Standard of Uniforms':
          ft=ft+int(d.rating6)
        if d.description=='Honesty and Integrity':
          ft=ft+int(d.rating6)
        if d.description=='Reward & Recognition':
          ft=ft+int(d.rating6)
        if d.description=='On time invoice submission':
          ft=ft+int(d.rating6)
        if d.description=='Training imparted to staff':
          ft=ft+int(d.rating6)
        if d.description=='Proactivness displayed by staff':
          ft=ft+int(d.rating6)
        if d.description=='Police verification document submission':
          ft=ft+int(d.rating6)
        if d.description=='Response time of vendor':
          ft=ft+int(d.rating6)
        if d.description=='Staff attrition':
          ft=ft+int(d.rating6)
        if d.description=='Supervisory skills of staff':
          ft=ft+int(d.rating6)
        if d.description=='General Total':
          d.rating6=ft
      count=count+16
      #msgprint(ft,count)
    if (self.doc.ga==1):
      for d in getlist(self.doclist, 've_details7'):
        if d.description=='Conduct of visits as per AMC':
          gt=gt+int(d.rating7)
        if d.description=='Skill of staff providing services':
          gt=gt+int(d.rating7)
        if d.description=='Response to calls for attending breakdowns or others issues':
          gt=gt+int(d.rating7)
        if d.description=='Organising work at site':
          gt=gt+int(d.rating7)
        if d.description=='Observing safety at site':
          gt=gt+int(d.rating7)
        if d.description=='Following rules/regulations of client/KF at site':
          gt=gt+int(d.rating7)
        if d.description=='Submission of service reports':
          gt=gt+int(d.rating7)
        if d.description=='AMC vendors Total':
          d.rating7=gt
      count=count+7

    # --------- Added Statutory Documents count in Final Summary -----
    monthly_doc_count = 0
    if self.doc.appointment_letter:
       monthly_doc_count += 1
    if self.doc.employment_cards:
       monthly_doc_count += 1
    if self.doc.wage_slips:
       monthly_doc_count += 1
    if self.doc.register_of_wages:
       monthly_doc_count += 1
    if self.doc.muster_roll:
       monthly_doc_count += 1
    if self.doc.sal_pay_proof:
       monthly_doc_count += 1
    if self.doc.register_wages_of_kf_fm:
       monthly_doc_count += 1
    if self.doc.leave_wage_register:
       monthly_doc_count += 1
    if self.doc.register_of_workmen:
       monthly_doc_count += 1
    if self.doc.register_of_deductions:
       monthly_doc_count += 1
    if self.doc.register_of_fines:
       monthly_doc_count += 1
    if self.doc.register_of_advances:
       monthly_doc_count += 1
    if self.doc.register_of_overtime:
       monthly_doc_count += 1
    if self.doc.deposit_summary_esi_pf:
       monthly_doc_count += 1
    if self.doc.pf_challan:
       monthly_doc_count += 1
    if self.doc.pf_ecr:
       monthly_doc_count += 1
    if self.doc.pf_remittance_confirmation_slips:
       monthly_doc_count += 1
    if self.doc.esi_challan:
       monthly_doc_count += 1
    if self.doc.copy_esi_card:
       monthly_doc_count += 1
    if self.doc.emp_monthly_contibution_history:
       monthly_doc_count += 1
    if self.doc.pf_esi_monthly_summary:
       monthly_doc_count += 1
    if self.doc.equal_remmuneration:
       monthly_doc_count += 1
    if self.doc.maternity_register:
       monthly_doc_count += 1
    if self.doc.service_certificate:
       monthly_doc_count += 1

    doc_list = []
    for i in getlist(self.doclist, 've_details'):
       doc_list.append(i.description)
       if i.description == "Monthly Documents":
          i.rating = monthly_doc_count

    if "Monthly Documents" not in doc_list :
       summry = addchild(self.doc, 've_details', 'VE Detail',1,self.doclist)
       summry.description = "Monthly Documents"
       summry.rating = monthly_doc_count

    #msgprint(count)
    count += monthly_doc_count
    #msgprint(count)

    if count > 0:
      tot=at+bt1+ct+dt+et+ft+gt+monthly_doc_count
      #msgprint("hi")
      #msgprint(monthly_doc_count)
      msgprint(tot)
      self.doc.maximum_points=count*5
      self.doc.minimum_points=count
      self.doc.vendor_points=tot
      self.doc.vendor_percentage = (flt(self.doc.vendor_points)/flt(self.doc.maximum_points))* 100

    if self.doc.vendor_percentage >= 90:
      self.doc.overall_performance = 'Excellent'
    elif self.doc.vendor_percentage <90 and self.doc.vendor_percentage >= 80:
      self.doc.overall_performance = 'Good'    
    elif self.doc.vendor_percentage <80 and self.doc.vendor_percentage >= 70:
      self.doc.overall_performance = 'Needs Improvement'
    elif self.doc.vendor_percentage <70:
      self.doc.overall_performance = 'Needs Replacement'   

    for d in getlist(self.doclist, 've_details'):
      if d.description=='A House keeping':
        d.rating=at
      if d.description=='B Technical':
        d.rating=bt1
      if d.description=='C Pantry Services':
        d.rating=ct
      if d.description=='D Horiculture':
        d.rating=dt
      if d.description=='E Security':
        d.rating=et
      if d.description=='F General':
        d.rating=ft
      if d.description=='G AMC vendors':
        d.rating=gt
      if d.description=='Total':
        d.rating=Total
      if d.description=='Average':
        d.rating=tot/count
      if d.description=='Percentage':
        d.rating=cstr(round(flt(self.doc.vendor_percentage),2)) 
      #if not self.doc.appointment_letter or not self.doc.employment_cards or not self.doc.wage_slips or not self.doc.register_of_wages or not self.doc.muster_roll or not self.doc.sal_pay_proof or not self.doc.register_wages_of_kf_fm or not self.doc.leave_wage_register or not self.doc.register_of_workmen or not self.doc.register_of_deductions or not self.doc.register_of_fines or not self.doc.register_of_advances or not self.doc.register_of_overtime or not self.doc.deposit_summary_esi_pf or not self.doc.pf_challan or not self.doc.pf_ecr or not self.doc.pf_remittance_confirmation_slips or not self.doc.esi_challan or not self.doc.copy_esi_card or not self.doc.emp_monthly_contibution_history or not self.doc.pf_esi_monthly_summary or not self.doc.equal_remmuneration or not self.doc.maternity_register or not self.doc.service_certificate :
       #  self.doc.vendor_points,self.doc.vendor_percentage,self.doc.standard_percentage,self.doc.overall_performance,d.rating=0 ,0,0,'Needs Replacement',0
        
    if self.doc.site_id:
       y="select site_name,client_id,client_name,region,kf_branch,location from tabSite where name='%s'"%(self.doc.site_id)
       x=sql(y)
       self.doc.site_name=x[0][0]
       self.doc.client_id=x[0][1]  
       self.doc.client_name=x[0][2]  
       self.doc.region=x[0][3]  
       self.doc.kf_branch=x[0][4]  
       self.doc.location =x[0][5]
    self.doc.evaluator_name=session['user']
    #if not self.doc.appointment_letter or not self.doc.employment_cards or not self.doc.wage_slips or not self.doc.register_of_wages or not self.doc.muster_roll or not self.doc.sal_pay_proof or not self.doc.register_wages_of_kf_fm or not self.doc.leave_wage_register or not self.doc.register_of_workmen or not self.doc.register_of_deductions or not self.doc.register_of_fines or not self.doc.register_of_advances or not self.doc.register_of_overtime or not self.doc.deposit_summary_esi_pf or not self.doc.pf_challan or not self.doc.pf_ecr or not self.doc.pf_remittance_confirmation_slips or not self.doc.esi_challan or not self.doc.copy_esi_card or not self.doc.emp_monthly_contibution_history or not self.doc.pf_esi_monthly_summary or not self.doc.equal_remmuneration or not self.doc.maternity_register or not self.doc.service_certificate :
     #    self.doc.vendor_points,self.doc.vendor_percentage,self.doc.standard_percentage,self.doc.overall_performance=0 ,0,0,'Needs Replacement'

    if not self.doc.vcode:
        import random
        self.doc.vcode=''.join(random.choice('0123456789ABCDEF') for i in range(16))

    self.doc.email_link='<a href="http://fms.kfcommunity.com/fms/images/logos/acknowledgement.html?vid='+self.doc.name+'&code='+cstr(self.doc.vcode)+'"><b>Click Here to Acknowledgement ..!</b></a>'
        