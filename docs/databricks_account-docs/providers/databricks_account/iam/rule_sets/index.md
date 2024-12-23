---
title: rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - rule_sets
  - iam
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>rule_sets</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.rule_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="grant_rules" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getruleset" /> | `SELECT` | <CopyableCode code="account_id, etag, name" /> | Get a rule set by its name. A rule set is always attached to a resource and contains a list of access rules on the said resource. Currently only a default rule set for each resource is supported. |
| <CopyableCode code="updateruleset" /> | `SELECT` | <CopyableCode code="account_id" /> | Replace the rules of a rule set. First, use  get to read the current version of the rule set before modifying it. This pattern helps prevent conflicts between concurrent updates. |

## `SELECT` examples

<Tabs
    defaultValue="updateruleset"
    values={[
        { label: 'rule_sets (updateruleset)', value: 'updateruleset' },
        { label: 'rule_sets (getruleset)', value: 'getruleset' }
    ]
}>
<TabItem value="updateruleset">

```sql
SELECT
name,
etag,
grant_rules
FROM databricks_account.iam.rule_sets
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="getruleset">

```sql
SELECT
name,
etag,
grant_rules
FROM databricks_account.iam.rule_sets
WHERE account_id = '{{ account_id }}' AND
etag = '{{ etag }}' AND
name = '{{ name }}';
```

</TabItem>
</Tabs>
