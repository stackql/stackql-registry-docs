---
title: vw_organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_organizations
  - org
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
<tr><td><b>Name</b></td><td><code>vw_organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.org.vw_organizations" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/confluent/v00.00.00000/services/org.yaml), located under `components -> x-stackQL-resources -> vw_organizations`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `text` |
| <CopyableCode code="api_version" /> | `text` |
| <CopyableCode code="created_at" /> | `text` |
| <CopyableCode code="display_name" /> | `text` |
| <CopyableCode code="jit_enabled" /> | `boolean` |
| <CopyableCode code="kind" /> | `text` |
| <CopyableCode code="resource_name" /> | `text` |
| <CopyableCode code="updated_at" /> | `text` |
## Methods
No additional methods available for this resource
