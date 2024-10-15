---
title: accounts_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_keys
  - maps
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

Creates, updates, deletes, gets or lists a <code>accounts_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps.accounts_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryKey" /> | `string` | The primary key for accessing the Maps REST APIs. |
| <CopyableCode code="primaryKeyLastUpdated" /> | `string` | The last updated date and time of the primary key. |
| <CopyableCode code="secondaryKey" /> | `string` | The secondary key for accessing the Maps REST APIs. |
| <CopyableCode code="secondaryKeyLastUpdated" /> | `string` | The last updated date and time of the secondary key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get the keys to use with the Maps APIs. A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration. |

## `SELECT` examples

Get the keys to use with the Maps APIs. A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.


```sql
SELECT
primaryKey,
primaryKeyLastUpdated,
secondaryKey,
secondaryKeyLastUpdated
FROM azure.maps.accounts_keys
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```