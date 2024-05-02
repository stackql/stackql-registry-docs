---
title: service_linked_role_deletion_status
hide_title: false
hide_table_of_contents: false
keywords:
  - service_linked_role_deletion_status
  - iam_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_linked_role_deletion_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam_api.service_linked_role_deletion_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Reason` | `object` | &lt;p&gt;The reason that the service-linked role deletion failed.&lt;/p&gt; &lt;p&gt;This data type is used as a response element in the &lt;a&gt;GetServiceLinkedRoleDeletionStatus&lt;/a&gt; operation.&lt;/p&gt; |
| `Status` | `string` | The status of the deletion. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `service_linked_role_deletion_status_Get` | `SELECT` | `DeletionTaskId, region` |
