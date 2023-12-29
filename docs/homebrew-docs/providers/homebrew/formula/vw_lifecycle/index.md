---
title: vw_lifecycle
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_lifecycle
  - formula
  - homebrew    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and report on Homebrew packages using SQL
custom_edit_url: null
image: /img/providers/homebrew/stackql-homebrew-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vw_lifecycle</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>homebrew.formula.vw_lifecycle</code></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/homebrew/v00.00.00000/services/formula.yaml), located under `components -> x-stackQL-resources -> vw_lifecycle`.

| Name | Datatype |
|:-----|:---------|
| `deprecated` | `boolean` |
| `deprecation_date` | `text` |
| `deprecation_reason` | `text` |
| `disable_date` | `text` |
| `disable_reason` | `text` |
| `disabled` | `boolean` |
| `formula_name` | `text` |
## Methods
No methods available for the resource
