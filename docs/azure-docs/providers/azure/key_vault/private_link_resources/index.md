---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `string` | Name of the key vault resource. |
| <CopyableCode code="location" /> | `string` | Azure location of the key vault resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
| <CopyableCode code="tags" /> | `object` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `string` | Resource type of the key vault resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_vault" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the private link resources supported for the key vault. |

## `SELECT` examples

Gets the private link resources supported for the key vault.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.key_vault.private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```