---
title: network_policies_external_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_policies_external_addresses
  - vmwareengine
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

Creates, updates, deletes or gets an <code>network_policies_external_address</code> resource or lists <code>network_policies_external_addresses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_policies_external_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.network_policies_external_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="externalAddresses" /> | `array` | A list of external IP addresses assigned to VMware workload VMs within the scope of the given network policy. |
| <CopyableCode code="nextPageToken" /> | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_external_addresses" /> | `SELECT` | <CopyableCode code="locationsId, networkPoliciesId, projectsId" /> | Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy. |

## `SELECT` examples

Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

```sql
SELECT
externalAddresses,
nextPageToken
FROM google.vmwareengine.network_policies_external_addresses
WHERE locationsId = '{{ locationsId }}'
AND networkPoliciesId = '{{ networkPoliciesId }}'
AND projectsId = '{{ projectsId }}'; 
```
