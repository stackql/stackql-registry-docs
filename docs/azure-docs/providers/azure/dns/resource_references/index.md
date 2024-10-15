---
title: resource_references
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_references
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

Creates, updates, deletes, gets or lists a <code>resource_references</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.resource_references" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The result of dns resource reference request. Returns a list of dns resource references for each of the azure resource in the request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_target_resources" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns the DNS records specified by the referencing targetResourceIds. |

## `SELECT` examples

Returns the DNS records specified by the referencing targetResourceIds.


```sql
SELECT
properties
FROM azure.dns.resource_references
WHERE subscriptionId = '{{ subscriptionId }}';
```