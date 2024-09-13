---
title: private_clouds_dns_forwarding
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds_dns_forwarding
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

Creates, updates, deletes, gets or lists a <code>private_clouds_dns_forwarding</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_clouds_dns_forwarding</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.private_clouds_dns_forwarding" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this DNS profile. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding` |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="forwardingRules" /> | `array` | Required. List of domain mappings to configure |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_dns_forwarding" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Gets details of the `DnsForwarding` config. |
| <CopyableCode code="update_dns_forwarding" /> | `UPDATE` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Updates the parameters of the `DnsForwarding` config, like associated domains. Only fields specified in `update_mask` are applied. |

## `SELECT` examples

Gets details of the `DnsForwarding` config.

```sql
SELECT
name,
createTime,
forwardingRules,
updateTime
FROM google.vmwareengine.private_clouds_dns_forwarding
WHERE locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>private_clouds_dns_forwarding</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.private_clouds_dns_forwarding
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
forwardingRules = '{{ forwardingRules }}'
WHERE 
locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```
