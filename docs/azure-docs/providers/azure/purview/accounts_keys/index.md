---
title: accounts_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_keys
  - purview
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.accounts_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="atlasKafkaPrimaryEndpoint" /> | `string` | Gets or sets the primary connection string. |
| <CopyableCode code="atlasKafkaSecondaryEndpoint" /> | `string` | Gets or sets the secondary connection string. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List the authorization keys associated with this account. |

## `SELECT` examples

List the authorization keys associated with this account.


```sql
SELECT
atlasKafkaPrimaryEndpoint,
atlasKafkaSecondaryEndpoint
FROM azure.purview.accounts_keys
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```