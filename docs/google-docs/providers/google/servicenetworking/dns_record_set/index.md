---
title: dns_record_set
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_record_set
  - servicenetworking
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

Creates, updates, deletes or gets an <code>dns_record_set</code> resource or lists <code>dns_record_set</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_record_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.dns_record_set" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `array` | Required. As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) for examples see https://cloud.google.com/dns/records/json-record. |
| <CopyableCode code="domain" /> | `string` | Required. The DNS or domain name of the record set, e.g. `test.example.com`. Cloud DNS requires that a DNS suffix ends with a trailing dot. |
| <CopyableCode code="ttl" /> | `string` | Required. The period of time for which this RecordSet can be cached by resolvers. |
| <CopyableCode code="type" /> | `string` | Required. The identifier of a supported record type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="servicesId" /> | Producers can use this method to retrieve information about the DNS record set added to the private zone inside the shared tenant host project associated with a consumer network. |

## `SELECT` examples

Producers can use this method to retrieve information about the DNS record set added to the private zone inside the shared tenant host project associated with a consumer network.

```sql
SELECT
data,
domain,
ttl,
type
FROM google.servicenetworking.dns_record_set
WHERE servicesId = '{{ servicesId }}'; 
```
