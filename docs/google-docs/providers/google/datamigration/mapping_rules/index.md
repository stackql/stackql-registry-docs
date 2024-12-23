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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>mapping_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mapping_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.mapping_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}. |
| <CopyableCode code="conditionalColumnSetValue" /> | `object` | Options to configure rule type ConditionalColumnSetValue. The rule is used to transform the data which is being replicated/migrated. The rule filter field can refer to one or more entities. The rule scope can be one of: Column. |
| <CopyableCode code="convertRowidColumn" /> | `object` | Options to configure rule type ConvertROWIDToColumn. The rule is used to add column rowid to destination tables based on an Oracle rowid function/property. The rule filter field can refer to one or more entities. The rule scope can be one of: Table. This rule requires additional filter to be specified beyond the basic rule filter field, which is whether or not to work on tables which already have a primary key defined. |
| <CopyableCode code="displayName" /> | `string` | Optional. A human readable name |
| <CopyableCode code="entityMove" /> | `object` | Options to configure rule type EntityMove. The rule is used to move an entity to a new schema. The rule filter field can refer to one or more entities. The rule scope can be one of: Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT |
| <CopyableCode code="filter" /> | `object` | A filter defining the entities that a mapping rule should be applied to. When more than one field is specified, the rule is applied only to entities which match all the fields. |
| <CopyableCode code="filterTableColumns" /> | `object` | Options to configure rule type FilterTableColumns. The rule is used to filter the list of columns to include or exclude from a table. The rule filter field can refer to one entity. The rule scope can be: Table Only one of the two lists can be specified for the rule. |
| <CopyableCode code="multiColumnDataTypeChange" /> | `object` | Options to configure rule type MultiColumnDatatypeChange. The rule is used to change the data type and associated properties of multiple columns at once. The rule filter field can refer to one or more entities. The rule scope can be one of:Column. This rule requires additional filters to be specified beyond the basic rule filter field, which is the source data type, but the rule supports additional filtering capabilities such as the minimum and maximum field length. All additional filters which are specified are required to be met in order for the rule to be applied (logical AND between the fields). |
| <CopyableCode code="multiEntityRename" /> | `object` | Options to configure rule type MultiEntityRename. The rule is used to rename multiple entities. The rule filter field can refer to one or more entities. The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp that the revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string. |
| <CopyableCode code="ruleOrder" /> | `string` | Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. |
| <CopyableCode code="ruleScope" /> | `string` | Required. The rule scope |
| <CopyableCode code="setTablePrimaryKey" /> | `object` | Options to configure rule type SetTablePrimaryKey. The rule is used to specify the columns and name to configure/alter the primary key of a table. The rule filter field can refer to one entity. The rule scope can be one of: Table. |
| <CopyableCode code="singleColumnChange" /> | `object` | Options to configure rule type SingleColumnChange. The rule is used to change the properties of a column. The rule filter field can refer to one entity. The rule scope can be one of: Column. When using this rule, if a field is not specified than the destination column's configuration will be the same as the one in the source column.. |
| <CopyableCode code="singleEntityRename" /> | `object` | Options to configure rule type SingleEntityRename. The rule is used to rename an entity. The rule filter field can refer to only one entity. The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT, Synonym |
| <CopyableCode code="singlePackageChange" /> | `object` | Options to configure rule type SinglePackageChange. The rule is used to alter the sql code for a package entities. The rule filter field can refer to one entity. The rule scope can be: Package |
| <CopyableCode code="sourceSqlChange" /> | `object` | Options to configure rule type SourceSqlChange. The rule is used to alter the sql code for database entities. The rule filter field can refer to one entity. The rule scope can be: StoredProcedure, Function, Trigger, View |
| <CopyableCode code="state" /> | `string` | Optional. The mapping rule state |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="conversionWorkspacesId, locationsId, mappingRulesId, projectsId" /> | Gets the details of a mapping rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Lists the mapping rules for a specific conversion workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Creates a new mapping rule for a given conversion workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="conversionWorkspacesId, locationsId, mappingRulesId, projectsId" /> | Deletes a single mapping rule. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files. |

## `SELECT` examples

Lists the mapping rules for a specific conversion workspace.

```sql
SELECT
name,
conditionalColumnSetValue,
convertRowidColumn,
displayName,
entityMove,
filter,
filterTableColumns,
multiColumnDataTypeChange,
multiEntityRename,
revisionCreateTime,
revisionId,
ruleOrder,
ruleScope,
setTablePrimaryKey,
singleColumnChange,
singleEntityRename,
singlePackageChange,
sourceSqlChange,
state
FROM google.datamigration.mapping_rules
WHERE conversionWorkspacesId = '{{ conversionWorkspacesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mapping_rules</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.datamigration.mapping_rules (
conversionWorkspacesId,
locationsId,
projectsId,
name,
displayName,
state,
ruleScope,
filter,
ruleOrder,
singleEntityRename,
multiEntityRename,
entityMove,
singleColumnChange,
multiColumnDataTypeChange,
conditionalColumnSetValue,
convertRowidColumn,
setTablePrimaryKey,
singlePackageChange,
sourceSqlChange,
filterTableColumns
)
SELECT 
'{{ conversionWorkspacesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ state }}',
'{{ ruleScope }}',
'{{ filter }}',
'{{ ruleOrder }}',
'{{ singleEntityRename }}',
'{{ multiEntityRename }}',
'{{ entityMove }}',
'{{ singleColumnChange }}',
'{{ multiColumnDataTypeChange }}',
'{{ conditionalColumnSetValue }}',
'{{ convertRowidColumn }}',
'{{ setTablePrimaryKey }}',
'{{ singlePackageChange }}',
'{{ sourceSqlChange }}',
'{{ filterTableColumns }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: state
      value: string
    - name: ruleScope
      value: string
    - name: filter
      value:
        - name: parentEntity
          value: string
        - name: entityNamePrefix
          value: string
        - name: entityNameSuffix
          value: string
        - name: entityNameContains
          value: string
        - name: entities
          value:
            - string
    - name: ruleOrder
      value: string
    - name: revisionId
      value: string
    - name: revisionCreateTime
      value: string
    - name: singleEntityRename
      value:
        - name: newName
          value: string
    - name: multiEntityRename
      value:
        - name: newNamePattern
          value: string
        - name: sourceNameTransformation
          value: string
    - name: entityMove
      value:
        - name: newSchema
          value: string
    - name: singleColumnChange
      value:
        - name: dataType
          value: string
        - name: charset
          value: string
        - name: collation
          value: string
        - name: length
          value: string
        - name: precision
          value: integer
        - name: scale
          value: integer
        - name: fractionalSecondsPrecision
          value: integer
        - name: array
          value: boolean
        - name: arrayLength
          value: integer
        - name: nullable
          value: boolean
        - name: autoGenerated
          value: boolean
        - name: udt
          value: boolean
        - name: customFeatures
          value: object
        - name: setValues
          value:
            - string
        - name: comment
          value: string
    - name: multiColumnDataTypeChange
      value:
        - name: sourceDataTypeFilter
          value: string
        - name: sourceTextFilter
          value:
            - name: sourceMinLengthFilter
              value: string
            - name: sourceMaxLengthFilter
              value: string
        - name: sourceNumericFilter
          value:
            - name: sourceMinScaleFilter
              value: integer
            - name: sourceMaxScaleFilter
              value: integer
            - name: sourceMinPrecisionFilter
              value: integer
            - name: sourceMaxPrecisionFilter
              value: integer
            - name: numericFilterOption
              value: string
        - name: newDataType
          value: string
        - name: overrideLength
          value: string
        - name: overrideScale
          value: integer
        - name: overridePrecision
          value: integer
        - name: overrideFractionalSecondsPrecision
          value: integer
        - name: customFeatures
          value: object
    - name: conditionalColumnSetValue
      value:
        - name: valueTransformation
          value:
            - name: isNull
              value: []
            - name: valueList
              value:
                - name: valuePresentList
                  value: string
                - name: values
                  value:
                    - string
                - name: ignoreCase
                  value: boolean
            - name: intComparison
              value:
                - name: valueComparison
                  value: string
                - name: value
                  value: string
            - name: doubleComparison
              value:
                - name: valueComparison
                  value: string
                - name: value
                  value: number
            - name: assignSpecificValue
              value:
                - name: value
                  value: string
            - name: roundScale
              value:
                - name: scale
                  value: integer
            - name: applyHash
              value: []
        - name: customFeatures
          value: object
    - name: convertRowidColumn
      value:
        - name: onlyIfNoPrimaryKey
          value: boolean
    - name: setTablePrimaryKey
      value:
        - name: primaryKeyColumns
          value:
            - string
        - name: primaryKey
          value: string
    - name: singlePackageChange
      value:
        - name: packageDescription
          value: string
        - name: packageBody
          value: string
    - name: sourceSqlChange
      value:
        - name: sqlCode
          value: string
    - name: filterTableColumns
      value:
        - name: includeColumns
          value:
            - string
        - name: excludeColumns
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>mapping_rules</code> resource.

```sql
/*+ delete */
DELETE FROM google.datamigration.mapping_rules
WHERE conversionWorkspacesId = '{{ conversionWorkspacesId }}'
AND locationsId = '{{ locationsId }}'
AND mappingRulesId = '{{ mappingRulesId }}'
AND projectsId = '{{ projectsId }}';
```
