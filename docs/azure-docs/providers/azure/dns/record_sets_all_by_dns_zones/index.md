---
title: record_sets_all_by_dns_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets_all_by_dns_zones
  - dns
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

Creates, updates, deletes, gets or lists a <code>record_sets_all_by_dns_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_sets_all_by_dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.record_sets_all_by_dns_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the record set. |
| <CopyableCode code="name" /> | `string` | The name of the record set. |
| <CopyableCode code="etag" /> | `string` | The etag of the record set. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the records in the record set. |
| <CopyableCode code="type" /> | `string` | The type of the record set. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Lists all record sets in a DNS zone. |

## `SELECT` examples

Lists all record sets in a DNS zone.


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.dns.record_sets_all_by_dns_zones
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```