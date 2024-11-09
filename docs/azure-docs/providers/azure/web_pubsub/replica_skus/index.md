---
title: replica_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_skus
  - web_pubsub
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

Creates, updates, deletes, gets or lists a <code>replica_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replica_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.replica_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Describes scaling information of a sku. |
| <CopyableCode code="resourceType" /> | `string` | The resource type that this object applies to |
| <CopyableCode code="sku" /> | `object` | The billing information of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | List all available skus of the replica resource. |

## `SELECT` examples

List all available skus of the replica resource.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.web_pubsub.replica_skus
WHERE replicaName = '{{ replicaName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```