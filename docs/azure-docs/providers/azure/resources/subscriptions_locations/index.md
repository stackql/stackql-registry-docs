---
title: subscriptions_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_locations
  - resources
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

Creates, updates, deletes, gets or lists a <code>subscriptions_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.subscriptions_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID of the location. For example, /subscriptions/8d65815f-a5b6-402f-9298-045155da7d74/locations/westus. |
| <CopyableCode code="name" /> | `string` | The location name. |
| <CopyableCode code="availabilityZoneMappings" /> | `array` | The availability zone mappings for this region. |
| <CopyableCode code="displayName" /> | `string` | The display name of the location. |
| <CopyableCode code="metadata" /> | `object` | Location metadata information |
| <CopyableCode code="regionalDisplayName" /> | `string` | The display name of the location and its region. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription ID. |
| <CopyableCode code="type" /> | `string` | The location type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list. |

## `SELECT` examples

This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list.


```sql
SELECT
id,
name,
availabilityZoneMappings,
displayName,
metadata,
regionalDisplayName,
subscriptionId,
type
FROM azure.resources.subscriptions_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```