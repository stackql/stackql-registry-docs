---
title: security_policies_preconfigured_expression_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies_preconfigured_expression_sets
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

Creates, updates, deletes, gets or lists a <code>security_policies_preconfigured_expression_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_policies_preconfigured_expression_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.security_policies_preconfigured_expression_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="preconfiguredExpressionSets" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_preconfigured_expression_sets" /> | `SELECT` | <CopyableCode code="project" /> | Gets the current list of preconfigured Web Application Firewall (WAF) expressions. |

## `SELECT` examples

Gets the current list of preconfigured Web Application Firewall (WAF) expressions.

```sql
SELECT
preconfiguredExpressionSets
FROM google.compute.security_policies_preconfigured_expression_sets
WHERE project = '{{ project }}'; 
```
