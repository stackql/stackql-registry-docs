---
title: active_security_admin_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - active_security_admin_rules
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

Creates, updates, deletes, gets or lists a <code>active_security_admin_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>active_security_admin_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.active_security_admin_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="commitTime" /> | `string` | Deployment time string. |
| <CopyableCode code="configurationDescription" /> | `string` | A description of the security admin configuration. |
| <CopyableCode code="kind" /> | `string` | Whether the rule is custom or default. |
| <CopyableCode code="region" /> | `string` | Deployment region. |
| <CopyableCode code="ruleCollectionAppliesToGroups" /> | `array` | Groups for rule collection |
| <CopyableCode code="ruleCollectionDescription" /> | `string` | A description of the rule collection. |
| <CopyableCode code="ruleGroups" /> | `array` | Effective configuration groups. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Lists active security admin rules in a network manager. |

## `SELECT` examples

Lists active security admin rules in a network manager.


```sql
SELECT
id,
commitTime,
configurationDescription,
kind,
region,
ruleCollectionAppliesToGroups,
ruleCollectionDescription,
ruleGroups
FROM azure.network.active_security_admin_rules
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```