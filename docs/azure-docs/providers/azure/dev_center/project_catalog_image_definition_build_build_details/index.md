---
title: project_catalog_image_definition_build_build_details
hide_title: false
hide_table_of_contents: false
keywords:
  - project_catalog_image_definition_build_build_details
  - dev_center
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>project_catalog_image_definition_build_build_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_catalog_image_definition_build_build_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.project_catalog_image_definition_build_build_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | End time of the task group. |
| <CopyableCode code="errorDetails" /> | `object` | Image creation error details |
| <CopyableCode code="imageReference" /> | `object` | Image reference information |
| <CopyableCode code="startTime" /> | `string` | Start time of the task group. |
| <CopyableCode code="status" /> | `string` | The state of an Image Definition Build. |
| <CopyableCode code="taskGroups" /> | `array` | The list of task groups executed during the image definition build. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, catalogName, imageDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Gets Build details |

## `SELECT` examples

Gets Build details


```sql
SELECT
endTime,
errorDetails,
imageReference,
startTime,
status,
taskGroups
FROM azure.dev_center.project_catalog_image_definition_build_build_details
WHERE buildName = '{{ buildName }}'
AND catalogName = '{{ catalogName }}'
AND imageDefinitionName = '{{ imageDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```