# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from InputForms.models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
accd = AllAccident.objects.defer("EmpName", "Narrative", "LearningPoint")
accd_r = accd.filter(EmpType='Regular')
accd_c = accd.filter(EmpType='Contract')


@login_required(login_url='/users/login_user/')
def summary(request):
    k = datetime.datetime.today()
    dt = k.day
    wk = k.isocalendar()[1]
    mn = k.month
    yr = k.year

    sdr = accd_r.filter(Date__year=yr, Date__month=mn, Date__day=dt)
    dfr = sdr.filter(AccdType='Fatal',).count()
    dfar = sdr.filter(AccdType='First-Aid',).count()
    drr = sdr.filter(AccdType='Reportable',).count()
    dnrr = sdr.filter(AccdType='Non-Reportable',).count()
    dtotalr = sdr.count()
    sdc = accd_c.filter(Date__year=yr, Date__month=mn, Date__day=dt)
    dfc = sdc.filter(AccdType='Fatal',).count()
    dfac = sdc.filter(AccdType='First-Aid',).count()
    drc = sdc.filter(AccdType='Reportable',).count()
    dnrc = sdc.filter(AccdType='Non-Reportable',).count()
    dtotalc = sdc.count()

    swr = accd_r.filter(Date__year=yr, Date__week=wk)
    wkfr = swr.filter(AccdType='Fatal',).count()
    wkfar = swr.filter(AccdType='First-Aid',).count()
    wkrr = swr.filter(AccdType='Reportable',).count()
    wknrr = swr.filter(AccdType='Non-Reportable',).count()
    wktotalr = swr.count()
    swc = accd_c.filter(Date__year=yr, Date__week=wk)
    wkfc = swc.filter(AccdType='Fatal',).count()
    wkfac = swc.filter(AccdType='First-Aid',).count()
    wkrc = swc.filter(AccdType='Reportable',).count()
    wknrc = swc.filter(AccdType='Non-Reportable',).count()
    wktotalc = swc.count()

    smr = accd_r.filter(Date__year=yr, Date__month=mn)
    mfr = smr.filter(AccdType='Fatal',).count()
    mfar = smr.filter(AccdType='First-Aid',).count()
    mrr = smr.filter(AccdType='Reportable',).count()
    mnrr = smr.filter(AccdType='Non-Reportable',).count()
    mtotalr = smr.count()
    smc = accd_c.filter(Date__year=yr, Date__month=mn)
    mfc = smc.filter(AccdType='Fatal',).count()
    mfac = smc.filter(AccdType='First-Aid',).count()
    mrc = smc.filter(AccdType='Reportable',).count()
    mnrc = smc.filter(AccdType='Non-Reportable',).count()
    mtotalc = smc.count()

    syr = accd_r.filter(Date__year=yr)
    yfr = syr.filter(AccdType='Fatal',).count()
    yfar = syr.filter(AccdType='First-Aid',).count()
    yrr = syr.filter(AccdType='Reportable',).count()
    ynrr = syr.filter(AccdType='Non-Reportable',).count()
    ytotalr = syr.count()
    syc = accd_c.filter(Date__year=yr)
    yfc = syc.filter(AccdType='Fatal',).count()
    yfac = syc.filter(AccdType='First-Aid',).count()
    yrc = syc.filter(AccdType='Reportable',).count()
    ynrc = syc.filter(AccdType='Non-Reportable',).count()
    ytotalc = syc.count()

    context = {
        'dfr': dfr, 'dfar': dfar, 'drr': drr, 'dnrr': dnrr, 'dtotalr': dtotalr,
        'dfc': dfc, 'dfac': dfac, 'drc': drc, 'dnrc': dnrc, 'dtotalc': dtotalc,

        'wkfr': wkfr, 'wkfar': wkfar, 'wkrr': wkrr, 'wknrr': wknrr, 'wktotalr': wktotalr,
        'wkfc': wkfc, 'wkfac': wkfac, 'wkrc': wkrc, 'wknrc': wknrc, 'wktotalc': wktotalc,

        'mfr': mfr, 'mfar': mfar, 'mrr': mrr, 'mnrr': mnrr, 'mtotalr': mtotalr,
        'mfc': mfc, 'mfac': mfac, 'mrc': mrc, 'mnrc': mnrc, 'mtotalc': mtotalc,

        'yfr': yfr, 'yfar': yfar, 'yrr': yrr, 'ynrr': ynrr, 'ytotalr': ytotalr,
        'yfc': yfc, 'yfac': yfac, 'yrc': yrc, 'ynrc': ynrc, 'ytotalc': ytotalc,
    }

    return render(request, 'Summary.html', context)
