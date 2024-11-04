---
title: acls
hide_title: false
hide_table_of_contents: false
keywords:
  - acls
  - kafka
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.acls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="host" /> | `string` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
| <CopyableCode code="operation" /> | `string` |
| <CopyableCode code="pattern_type" /> | `string` |
| <CopyableCode code="permission" /> | `string` |
| <CopyableCode code="principal" /> | `string` |
| <CopyableCode code="resource_name" /> | `string` |
| <CopyableCode code="resource_type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_acls" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return a list of ACLs that match the search criteria. |
| <CopyableCode code="create_kafka_acls" /> | `INSERT` | <CopyableCode code="cluster_id, data__host, data__operation, data__pattern_type, data__permission, data__principal, data__resource_name, data__resource_type" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Create an ACL. |
| <CopyableCode code="delete_kafka_acls" /> | `DELETE` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Delete the ACLs that match the search criteria. |
| <CopyableCode code="batch_create_kafka_acls" /> | `EXEC` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Create ACLs. |
