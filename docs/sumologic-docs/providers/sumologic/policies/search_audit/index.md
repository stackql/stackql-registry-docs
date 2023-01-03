---
title: search_audit
hide_title: false
hide_table_of_contents: false
keywords:
  - search_audit
  - policies
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>search_audit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.policies.search_audit</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getSearchAuditPolicy` | `SELECT` |  | Get the Search Audit policy. This policy specifies whether search records for your account are enabled. You can access details about your account's search capacity, queries run by users from the Sumo Search Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Search_Audit_Index) |
| `setSearchAuditPolicy` | `EXEC` | `data__enabled` | Set the Search Audit policy. This policy specifies whether search records for your account are enabled. You can access details about your account's search capacity, queries run by users from the Sumo Search Audit Index. [Learn More](https://help.sumologic.com/Manage/Security/Search_Audit_Index) |
