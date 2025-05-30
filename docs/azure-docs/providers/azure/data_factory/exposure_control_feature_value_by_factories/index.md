---
title: exposure_control_feature_value_by_factories
hide_title: false
hide_table_of_contents: false
keywords:
  - exposure_control_feature_value_by_factories
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>exposure_control_feature_value_by_factories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exposure_control_feature_value_by_factories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.exposure_control_feature_value_by_factories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="featureName" /> | `string` | The feature name. |
| <CopyableCode code="value" /> | `string` | The feature value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Get exposure control feature for specific factory. |

## `SELECT` examples

Get exposure control feature for specific factory.


```sql
SELECT
featureName,
value
FROM azure.data_factory.exposure_control_feature_value_by_factories
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```