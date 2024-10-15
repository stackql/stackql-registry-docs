---
title: component_current_billing_features
hide_title: false
hide_table_of_contents: false
keywords:
  - component_current_billing_features
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>component_current_billing_features</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_current_billing_features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.component_current_billing_features" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="CurrentBillingFeatures" /> | `array` | Current enabled pricing plan. When the component is in the Enterprise plan, this will list both 'Basic' and 'Application Insights Enterprise'. |
| <CopyableCode code="DataVolumeCap" /> | `object` | An Application Insights component daily data volume cap |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns current billing features for an Application Insights component. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update current billing features for an Application Insights component. |

## `SELECT` examples

Returns current billing features for an Application Insights component.


```sql
SELECT
CurrentBillingFeatures,
DataVolumeCap
FROM azure.application_insights.component_current_billing_features
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>component_current_billing_features</code> resource.

```sql
/*+ update */
REPLACE azure.application_insights.component_current_billing_features
SET 
DataVolumeCap = '{{ DataVolumeCap }}',
CurrentBillingFeatures = '{{ CurrentBillingFeatures }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
