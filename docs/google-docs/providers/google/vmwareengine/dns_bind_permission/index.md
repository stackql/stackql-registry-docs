---
title: dns_bind_permission
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_bind_permission
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

Creates, updates, deletes or gets an <code>dns_bind_permission</code> resource or lists <code>dns_bind_permission</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_bind_permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.dns_bind_permission" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Output only. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource and location can only be global. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/dnsBindPermission` |
| <CopyableCode code="principals" /> | `array` | Output only. Users/Service accounts which have access for binding on the intranet VPC project corresponding to the consumer project. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_dns_bind_permission" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global. |
| <CopyableCode code="grant" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global. |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global. |

## `SELECT` examples

Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global.

```sql
SELECT
name,
principals
FROM google.vmwareengine.dns_bind_permission
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
