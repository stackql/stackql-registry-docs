---
title: tenant_level_access_review_instance_contacted_reviewers
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_level_access_review_instance_contacted_reviewers
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_level_access_review_instance_contacted_reviewers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.tenant_level_access_review_instance_contacted_reviewers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review reviewer id. |
| `name` | `string` | The access review reviewer id. |
| `properties` | `object` | Properties of access review contacted reviewer. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `TenantLevelAccessReviewInstanceContactedReviewers_List` | `SELECT` | `id, scheduleDefinitionId` |
