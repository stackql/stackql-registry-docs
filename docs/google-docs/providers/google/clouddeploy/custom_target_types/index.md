---
title: custom_target_types
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_target_types
  - clouddeploy
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_target_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.custom_target_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `CustomTargetType`. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/customTargetTypes/&#123;customTargetType&#125;`. The `customTargetType` component must match `[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Optional. Description of the `CustomTargetType`. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `CustomTargetType` was created. |
| <CopyableCode code="customActions" /> | `object` | CustomTargetSkaffoldActions represents the `CustomTargetType` configuration using Skaffold custom actions. |
| <CopyableCode code="customTargetTypeId" /> | `string` | Output only. Resource id of the `CustomTargetType`. |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `CustomTargetType`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Most recent time at which the `CustomTargetType` was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customTargetTypesId, locationsId, projectsId" /> | Gets details of a single CustomTargetType. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CustomTargetTypes in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new CustomTargetType in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customTargetTypesId, locationsId, projectsId" /> | Deletes a single CustomTargetType. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="customTargetTypesId, locationsId, projectsId" /> | Updates a single CustomTargetType. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists CustomTargetTypes in a given project and location. |
