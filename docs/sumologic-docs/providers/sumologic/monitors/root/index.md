---
title: root
hide_title: false
hide_table_of_contents: false
keywords:
  - root
  - monitors
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>root</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.monitors.root" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the monitor or folder. |
| <CopyableCode code="name" /> | `string` | Identifier of the monitor or folder. |
| <CopyableCode code="description" /> | `string` | Description of the monitor or folder. |
| <CopyableCode code="_permissions" /> | `array` | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. |
| <CopyableCode code="children" /> | `array` | Children of the folder. NOTE: Permissions field will not be filled (empty list) for children. |
| <CopyableCode code="contentType" /> | `string` | Type of the content. Valid values:<br />  1) Monitor<br />  2) Folder |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="isMutable" /> | `boolean` | Immutable objects are "READ-ONLY". |
| <CopyableCode code="isSystem" /> | `boolean` | System objects are objects provided by Sumo Logic. System objects can only be localized. Non-local fields can't be updated. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="parentId" /> | `string` | Identifier of the parent folder. |
| <CopyableCode code="permissions" /> | `array` | Aggregated permission summary for the calling user. If detailed permission statements are required, please call list permissions endpoint. |
| <CopyableCode code="type" /> | `string` | Type of the object model. |
| <CopyableCode code="version" /> | `integer` | Version of the monitor or folder. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getMonitorsLibraryRoot" /> | `SELECT` | <CopyableCode code="region" /> |
