---
title: managers_feature_support_status
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_feature_support_status
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>managers_feature_support_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers_feature_support_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.managers_feature_support_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the feature. |
| <CopyableCode code="status" /> | `string` | The feature support status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Lists the features and their support status |

## `SELECT` examples

Lists the features and their support status


```sql
SELECT
name,
status
FROM azure_extras.storsimple_8000_series.managers_feature_support_status
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```