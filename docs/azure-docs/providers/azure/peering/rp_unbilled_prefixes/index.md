---
title: rp_unbilled_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - rp_unbilled_prefixes
  - peering
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

Creates, updates, deletes, gets or lists a <code>rp_unbilled_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rp_unbilled_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.rp_unbilled_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureRegion" /> | `string` | The Azure region. |
| <CopyableCode code="peerAsn" /> | `integer` | The peer ASN. |
| <CopyableCode code="prefix" /> | `string` | The prefix. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Lists all of the RP unbilled prefixes for the specified peering |

## `SELECT` examples

Lists all of the RP unbilled prefixes for the specified peering


```sql
SELECT
azureRegion,
peerAsn,
prefix
FROM azure.peering.rp_unbilled_prefixes
WHERE peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```