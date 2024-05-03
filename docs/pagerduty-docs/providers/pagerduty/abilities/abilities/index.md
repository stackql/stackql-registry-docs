---
title: abilities
hide_title: false
hide_table_of_contents: false
keywords:
  - abilities
  - abilities
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>abilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.abilities.abilities" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_abilities" /> | `SELECT` |  | List all of your account's abilities, by name.<br /><br />"Abilities" describes your account's capabilities by feature name. For example `"teams"`.<br /><br />An ability may be available to your account based on things like your pricing plan or account state.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#abilities)<br /><br />Scoped OAuth requires: `abilities.read`<br /> |
| <CopyableCode code="_list_abilities" /> | `EXEC` |  | List all of your account's abilities, by name.<br /><br />"Abilities" describes your account's capabilities by feature name. For example `"teams"`.<br /><br />An ability may be available to your account based on things like your pricing plan or account state.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#abilities)<br /><br />Scoped OAuth requires: `abilities.read`<br /> |
| <CopyableCode code="get_ability" /> | `EXEC` | <CopyableCode code="id" /> | Test whether your account has a given ability.<br /><br />"Abilities" describes your account's capabilities by feature name. For example `"teams"`.<br /><br />An ability may be available to your account based on things like your pricing plan or account state.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#abilities)<br /><br />Scoped OAuth requires: `abilities.read`<br /> |
