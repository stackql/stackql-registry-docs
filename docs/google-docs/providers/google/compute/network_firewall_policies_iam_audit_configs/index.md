---
title: network_firewall_policies_iam_audit_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - network_firewall_policies_iam_audit_configs
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_firewall_policies_iam_audit_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.network_firewall_policies_iam_audit_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `auditLogConfigs` | `array` | The configuration for logging of each type of permission. |
| `exemptedMembers` | `array` | This is deprecated and has no effect. Do not use. |
| `service` | `string` | Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `networkFirewallPolicies_getIamPolicy` | `SELECT` | `project, resource` |
