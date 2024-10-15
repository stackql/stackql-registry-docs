---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - storage
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

Creates, updates, deletes, gets or lists a <code>skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The SKU name. Required for account creation; optional for update. Note that in older versions, SKU name was called accountType. |
| <CopyableCode code="capabilities" /> | `array` | The capability information in the specified SKU, including file encryption, network ACLs, change notification, etc. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of storage account. |
| <CopyableCode code="locations" /> | `array` | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |
| <CopyableCode code="resourceType" /> | `string` | The type of the resource, usually it is 'storageAccounts'. |
| <CopyableCode code="restrictions" /> | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| <CopyableCode code="tier" /> | `string` | The SKU tier. This is based on the SKU name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the available SKUs supported by Microsoft.Storage for given subscription. |

## `SELECT` examples

Lists the available SKUs supported by Microsoft.Storage for given subscription.


```sql
SELECT
name,
capabilities,
kind,
locations,
resourceType,
restrictions,
tier
FROM azure.storage.skus
WHERE subscriptionId = '{{ subscriptionId }}';
```