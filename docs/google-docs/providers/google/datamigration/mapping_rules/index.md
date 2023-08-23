---
title: mapping_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - mapping_rules
  - datamigration
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
<tr><td><b>Name</b></td><td><code>mapping_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.mapping_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of the mapping rule resource, in the form of: projects/&#123;project&#125;/locations/&#123;location&#125;/conversionWorkspaces/&#123;set&#125;/mappingRule/&#123;rule&#125;. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `state` | `string` | Optional. The mapping rule state |
| `filterTableColumns` | `object` | Options to configure rule type FilterTableColumns. The rule is used to filter the list of columns to include or exclude from a table. The rule filter field can refer to one entity. The rule scope can be: Table Only one of the two lists can be specified for the rule. |
| `convertRowidColumn` | `object` | Options to configure rule type ConvertROWIDToColumn. The rule is used to add column rowid to destination tables based on an Oracle rowid function/property. The rule filter field can refer to one or more entities. The rule scope can be one of: Table. This rule requires additional filter to be specified beyond the basic rule filter field, which is whether or not to work on tables which already have a primary key defined. |
| `ruleOrder` | `string` | Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. |
| `filter` | `object` | A filter defining the entities that a mapping rule should be applied to. When more than one field is specified, the rule is applied only to entities which match all the fields. |
| `setTablePrimaryKey` | `object` | Options to configure rule type SetTablePrimaryKey. The rule is used to specify the columns and name to configure/alter the primary key of a table. The rule filter field can refer to one entity. The rule scope can be one of: Table. |
| `entityMove` | `object` | Options to configure rule type EntityMove. The rule is used to move an entity to a new schema. The rule filter field can refer to one or more entities. The rule scope can be one of: Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT |
| `ruleScope` | `string` | Required. The rule scope |
| `displayName` | `string` | Optional. A human readable name |
| `multiColumnDataTypeChange` | `object` | Options to configure rule type MultiColumnDatatypeChange. The rule is used to change the data type and associated properties of multiple columns at once. The rule filter field can refer to one or more entities. The rule scope can be one of:Column. This rule requires additional filters to be specified beyond the basic rule filter field, which is the source data type, but the rule supports additional filtering capabilities such as the minimum and maximum field length. All additional filters which are specified are required to be met in order for the rule to be applied (logical AND between the fields). |
| `multiEntityRename` | `object` | Options to configure rule type MultiEntityRename. The rule is used to rename multiple entities. The rule filter field can refer to one or more entities. The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT |
| `sourceSqlChange` | `object` | Options to configure rule type SourceSqlChange. The rule is used to alter the sql code for database entities. The rule filter field can refer to one entity. The rule scope can be: StoredProcedure, Function, Trigger, View |
| `conditionalColumnSetValue` | `object` | Options to configure rule type ConditionalColumnSetValue. The rule is used to transform the data which is being replicated/migrated. The rule filter field can refer to one or more entities. The rule scope can be one of: Column. |
| `singlePackageChange` | `object` | Options to configure rule type SinglePackageChange. The rule is used to alter the sql code for a package entities. The rule filter field can refer to one entity. The rule scope can be: Package |
| `singleColumnChange` | `object` | Options to configure rule type SingleColumnChange. The rule is used to change the properties of a column. The rule filter field can refer to one entity. The rule scope can be one of: Column. When using this rule, if a field is not specified than the destination column's configuration will be the same as the one in the source column.. |
| `singleEntityRename` | `object` | Options to configure rule type SingleEntityRename. The rule is used to rename an entity. The rule filter field can refer to only one entity. The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT, Synonym |
| `revisionId` | `string` | Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `conversionWorkspacesId, locationsId, mappingRulesId, projectsId` | Gets the details of a mapping rule. |
| `list` | `SELECT` | `conversionWorkspacesId, locationsId, projectsId` | Lists the mapping rules for a specific conversion workspace. |
| `create` | `INSERT` | `conversionWorkspacesId, locationsId, projectsId` | Creates a new mapping rule for a given conversion workspace. |
| `delete` | `DELETE` | `conversionWorkspacesId, locationsId, mappingRulesId, projectsId` | Deletes a single mapping rule. |
| `_list` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Lists the mapping rules for a specific conversion workspace. |
| `import` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files. |
