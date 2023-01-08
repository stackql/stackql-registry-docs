---
title: rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_sets
  - contentwarehouse
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.rule_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the rule set. Managed internally. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/ruleSet/&#123;rule_set_id&#125;. The name is ignored when creating a rule set. |
| `description` | `string` | Short description of the rule-set. |
| `rules` | `array` | List of rules given by the customer. |
| `source` | `string` | Source of the rules i.e., customer name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_ruleSets_get` | `SELECT` | `locationsId, projectsId, ruleSetsId` | Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist. |
| `projects_locations_ruleSets_list` | `SELECT` | `locationsId, projectsId` | Lists rulesets. |
| `projects_locations_ruleSets_create` | `INSERT` | `locationsId, projectsId` | Creates a ruleset. |
| `projects_locations_ruleSets_delete` | `DELETE` | `locationsId, projectsId, ruleSetsId` | Deletes a ruleset. Returns NOT_FOUND if the document does not exist. |
| `projects_locations_ruleSets_patch` | `EXEC` | `locationsId, projectsId, ruleSetsId` | Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name. |
