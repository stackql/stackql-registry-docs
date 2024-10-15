---
title: customization_tasks_error_details
hide_title: false
hide_table_of_contents: false
keywords:
  - customization_tasks_error_details
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

Creates, updates, deletes, gets or lists a <code>customization_tasks_error_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customization_tasks_error_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.customization_tasks_error_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="errors" /> | `array` | Errors associated with resources synchronized from the catalog. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId, taskName" /> | Gets Customization Task error details |

## `SELECT` examples

Gets Customization Task error details


```sql
SELECT
errors
FROM azure.dev_center.customization_tasks_error_details
WHERE catalogName = '{{ catalogName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```