---
title: guest_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_configuration
  - azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

Guest Configuration definitions in Azure Policy allow you to validate settings inside virtual machines. This validation includes the configuration of the operating system, applications, or even environmental data. You can use this API to create or update a Guest Configuration, and get information about the compliance details of a virtual machine. The details include specific settings that arent compliant with the assigned configuration.  
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>9</b></span><br />
<span>total selectable resources:&nbsp;<b>9</b></span><br />
<span>total methods:&nbsp;<b>27</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure.guest_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Azure Policy Guest Configuration</td></tr>
<tr><td><b>Description</b></td><td>Guest Configuration definitions in Azure Policy allow you to validate settings inside virtual machines. This validation includes the configuration of the operating system, applications, or even environmental data. You can use this API to create or update a Guest Configuration, and get information about the compliance details of a virtual machine. The details include specific settings that arent compliant with the assigned configuration.</td></tr>
<tr><td><b>Id</b></td><td><code>azure:guest_configuration</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/guest_configuration/assignment_reports/">assignment_reports</a><br />
<a href="/providers/azure/guest_configuration/assignment_reports_vm_ss/">assignment_reports_vm_ss</a><br />
<a href="/providers/azure/guest_configuration/assignments/">assignments</a><br />
<a href="/providers/azure/guest_configuration/assignments_vm_ss/">assignments_vm_ss</a><br />
<a href="/providers/azure/guest_configuration/connected_vmwarev_sphere_assignments/">connected_vmwarev_sphere_assignments</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/guest_configuration/connected_vmwarev_sphere_assignments_reports/">connected_vmwarev_sphere_assignments_reports</a><br />
<a href="/providers/azure/guest_configuration/hcrp_assignment_reports/">hcrp_assignment_reports</a><br />
<a href="/providers/azure/guest_configuration/hcrp_assignments/">hcrp_assignments</a><br />
<a href="/providers/azure/guest_configuration/operations/">operations</a><br />
</div>
</div>
