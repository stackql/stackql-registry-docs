---
title: move_collections_move_collections_by_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections_move_collections_by_subscriptions
  - resource_mover
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

Creates, updates, deletes, gets or lists a <code>move_collections_move_collections_by_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>move_collections_move_collections_by_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.move_collections_move_collections_by_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | The etag of the resource. |
| <CopyableCode code="identity" /> | `object` | Defines the MSI properties of the Move Collection. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="properties" /> | `object` | Defines the move collection properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the Move Collections in the subscription. |

## `SELECT` examples

Get all the Move Collections in the subscription.


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
systemData,
tags,
type
FROM azure.resource_mover.move_collections_move_collections_by_subscriptions
WHERE subscriptionId = '{{ subscriptionId }}';
```