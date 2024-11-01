---
title: connectors_with_expansions
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors_with_expansions
  - connect
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
<tr><td><b>Name</b></td><td><code>connectors_with_expansions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connectors_with_expansions" /></td></tr>
</tbody></table>

## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_connectv1connectors_with_expansions" /> | `SELECT` | <CopyableCode code="environment_id, kafka_cluster_id" /> |
