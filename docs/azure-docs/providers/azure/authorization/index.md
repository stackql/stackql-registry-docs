---
title: authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization
  - azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
You Use Role-Based Access Control To Manage The Actions Users In Your Organization Can Take On Resources. This Set Of Operations Enables You To Define Roles, Assign Roles To Users Or Groups, And Get Information About Permissions.  
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>66</b></span><br />
<span>total selectable resources:&nbsp;<b>59</b></span><br />
<span>total methods:&nbsp;<b>164</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure.authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Authorization</td></tr>
<tr><td><b>Description</b></td><td>You Use Role-Based Access Control To Manage The Actions Users In Your Organization Can Take On Resources. This Set Of Operations Enables You To Define Roles, Assign Roles To Users Or Groups, And Get Information About Permissions.</td></tr>
<tr><td><b>Id</b></td><td><code>authorization:v24.01.00201</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/authorization/access_review_default_settings/">access_review_default_settings</a><br />
<a href="/providers/azure/authorization/access_review_history_definition/">access_review_history_definition</a><br />
<a href="/providers/azure/authorization/access_review_history_definition_instance/">access_review_history_definition_instance</a><br />
<a href="/providers/azure/authorization/access_review_history_definition_instances/">access_review_history_definition_instances</a><br />
<a href="/providers/azure/authorization/access_review_history_definitions/">access_review_history_definitions</a><br />
<a href="/providers/azure/authorization/access_review_instance/">access_review_instance</a><br />
<a href="/providers/azure/authorization/access_review_instance_contacted_reviewers/">access_review_instance_contacted_reviewers</a><br />
<a href="/providers/azure/authorization/access_review_instance_decisions/">access_review_instance_decisions</a><br />
<a href="/providers/azure/authorization/access_review_instance_my_decisions/">access_review_instance_my_decisions</a><br />
<a href="/providers/azure/authorization/access_review_instances/">access_review_instances</a><br />
<a href="/providers/azure/authorization/access_review_instances_assigned_for_my_approval/">access_review_instances_assigned_for_my_approval</a><br />
<a href="/providers/azure/authorization/access_review_schedule_definitions/">access_review_schedule_definitions</a><br />
<a href="/providers/azure/authorization/access_review_schedule_definitions_assigned_for_my_approval/">access_review_schedule_definitions_assigned_for_my_approval</a><br />
<a href="/providers/azure/authorization/alert_configurations/">alert_configurations</a><br />
<a href="/providers/azure/authorization/alert_configurations_for_scope/">alert_configurations_for_scope</a><br />
<a href="/providers/azure/authorization/alert_definitions/">alert_definitions</a><br />
<a href="/providers/azure/authorization/alert_definitions_for_scope/">alert_definitions_for_scope</a><br />
<a href="/providers/azure/authorization/alert_incidents/">alert_incidents</a><br />
<a href="/providers/azure/authorization/alert_incidents_for_scope/">alert_incidents_for_scope</a><br />
<a href="/providers/azure/authorization/alert_operation/">alert_operation</a><br />
<a href="/providers/azure/authorization/alerts/">alerts</a><br />
<a href="/providers/azure/authorization/alerts_for_scope/">alerts_for_scope</a><br />
<a href="/providers/azure/authorization/classic_administrators/">classic_administrators</a><br />
<a href="/providers/azure/authorization/deny_assignments/">deny_assignments</a><br />
<a href="/providers/azure/authorization/deny_assignments_for_resource/">deny_assignments_for_resource</a><br />
<a href="/providers/azure/authorization/deny_assignments_for_resource_group/">deny_assignments_for_resource_group</a><br />
<a href="/providers/azure/authorization/deny_assignments_for_scope/">deny_assignments_for_scope</a><br />
<a href="/providers/azure/authorization/eligible_child_resources/">eligible_child_resources</a><br />
<a href="/providers/azure/authorization/global_administrator/">global_administrator</a><br />
<a href="/providers/azure/authorization/operations/">operations</a><br />
<a href="/providers/azure/authorization/permissions_for_resource/">permissions_for_resource</a><br />
<a href="/providers/azure/authorization/permissions_for_resource_group/">permissions_for_resource_group</a><br />
<a href="/providers/azure/authorization/provider_operations_metadata/">provider_operations_metadata</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/authorization/role_assignment_schedule_instances/">role_assignment_schedule_instances</a><br />
<a href="/providers/azure/authorization/role_assignment_schedule_instances_for_scope/">role_assignment_schedule_instances_for_scope</a><br />
<a href="/providers/azure/authorization/role_assignment_schedule_requests/">role_assignment_schedule_requests</a><br />
<a href="/providers/azure/authorization/role_assignment_schedule_requests_for_scope/">role_assignment_schedule_requests_for_scope</a><br />
<a href="/providers/azure/authorization/role_assignment_schedules/">role_assignment_schedules</a><br />
<a href="/providers/azure/authorization/role_assignment_schedules_for_scope/">role_assignment_schedules_for_scope</a><br />
<a href="/providers/azure/authorization/role_assignments/">role_assignments</a><br />
<a href="/providers/azure/authorization/role_assignments_for_resource/">role_assignments_for_resource</a><br />
<a href="/providers/azure/authorization/role_assignments_for_resource_group/">role_assignments_for_resource_group</a><br />
<a href="/providers/azure/authorization/role_assignments_for_scope/">role_assignments_for_scope</a><br />
<a href="/providers/azure/authorization/role_assignments_for_subscription/">role_assignments_for_subscription</a><br />
<a href="/providers/azure/authorization/role_definitions/">role_definitions</a><br />
<a href="/providers/azure/authorization/role_eligibility_schedule_instances/">role_eligibility_schedule_instances</a><br />
<a href="/providers/azure/authorization/role_eligibility_schedule_instances_for_scope/">role_eligibility_schedule_instances_for_scope</a><br />
<a href="/providers/azure/authorization/role_eligibility_schedule_requests/">role_eligibility_schedule_requests</a><br />
<a href="/providers/azure/authorization/role_eligibility_schedule_requests_for_scope/">role_eligibility_schedule_requests_for_scope</a><br />
<a href="/providers/azure/authorization/role_eligibility_schedules/">role_eligibility_schedules</a><br />
<a href="/providers/azure/authorization/role_eligibility_schedules_for_scope/">role_eligibility_schedules_for_scope</a><br />
<a href="/providers/azure/authorization/role_management_policies/">role_management_policies</a><br />
<a href="/providers/azure/authorization/role_management_policies_for_scope/">role_management_policies_for_scope</a><br />
<a href="/providers/azure/authorization/role_management_policy_assignments/">role_management_policy_assignments</a><br />
<a href="/providers/azure/authorization/role_management_policy_assignments_for_scope/">role_management_policy_assignments_for_scope</a><br />
<a href="/providers/azure/authorization/scope_access_review_default_settings/">scope_access_review_default_settings</a><br />
<a href="/providers/azure/authorization/scope_access_review_history_definition/">scope_access_review_history_definition</a><br />
<a href="/providers/azure/authorization/scope_access_review_history_definition_instance/">scope_access_review_history_definition_instance</a><br />
<a href="/providers/azure/authorization/scope_access_review_history_definition_instances/">scope_access_review_history_definition_instances</a><br />
<a href="/providers/azure/authorization/scope_access_review_history_definitions/">scope_access_review_history_definitions</a><br />
<a href="/providers/azure/authorization/scope_access_review_instance/">scope_access_review_instance</a><br />
<a href="/providers/azure/authorization/scope_access_review_instance_contacted_reviewers/">scope_access_review_instance_contacted_reviewers</a><br />
<a href="/providers/azure/authorization/scope_access_review_instance_decisions/">scope_access_review_instance_decisions</a><br />
<a href="/providers/azure/authorization/scope_access_review_instances/">scope_access_review_instances</a><br />
<a href="/providers/azure/authorization/scope_access_review_schedule_definitions/">scope_access_review_schedule_definitions</a><br />
<a href="/providers/azure/authorization/tenant_level_access_review_instance_contacted_reviewers/">tenant_level_access_review_instance_contacted_reviewers</a><br />
</div>
</div>
