---
title: application_gateways_available_ssl_predefined_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways_available_ssl_predefined_policies
  - network
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

Creates, updates, deletes, gets or lists a <code>application_gateways_available_ssl_predefined_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateways_available_ssl_predefined_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways_available_ssl_predefined_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the Ssl predefined policy. |
| <CopyableCode code="properties" /> | `object` | Properties of ApplicationGatewaySslPredefinedPolicy. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all SSL predefined policies for configuring Ssl policy. |

## `SELECT` examples

Lists all SSL predefined policies for configuring Ssl policy.


```sql
SELECT
id,
name,
properties
FROM azure.network.application_gateways_available_ssl_predefined_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```