---
title: cloud_services_update_domain_update_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_update_domain_update_domains
  - compute
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

Creates, updates, deletes, gets or lists a <code>cloud_services_update_domain_update_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_services_update_domain_update_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_services_update_domain_update_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, updateDomain" /> | Gets the specified update domain of a cloud service. Use nextLink property in the response to get the next page of update domains. Do this till nextLink is null to fetch all the update domains. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets a list of all update domains in a cloud service. |

## `SELECT` examples

Gets a list of all update domains in a cloud service.


```sql
SELECT
id,
name
FROM azure.compute.cloud_services_update_domain_update_domains
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```