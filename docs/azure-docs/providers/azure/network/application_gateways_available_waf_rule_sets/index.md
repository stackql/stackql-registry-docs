---
title: application_gateways_available_waf_rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways_available_waf_rule_sets
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

Creates, updates, deletes, gets or lists a <code>application_gateways_available_waf_rule_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateways_available_waf_rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways_available_waf_rule_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the web application firewall rule set. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all available web application firewall rule sets. |

## `SELECT` examples

Lists all available web application firewall rule sets.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.network.application_gateways_available_waf_rule_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```