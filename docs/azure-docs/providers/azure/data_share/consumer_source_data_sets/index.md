---
title: consumer_source_data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_source_data_sets
  - data_share
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

Creates, updates, deletes, gets or lists a <code>consumer_source_data_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_source_data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.consumer_source_data_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Properties of consumer source dataSet |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_share_subscription" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Get source dataSets of a shareSubscription |

## `SELECT` examples

Get source dataSets of a shareSubscription


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_share.consumer_source_data_sets
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareSubscriptionName = '{{ shareSubscriptionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```