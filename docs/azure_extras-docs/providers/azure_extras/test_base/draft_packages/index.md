---
title: draft_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - draft_packages
  - test_base
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

Creates, updates, deletes, gets or lists a <code>draft_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>draft_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.draft_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_draft_packages', value: 'view', },
        { label: 'draft_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="comments" /> | `text` | field from the `properties` object |
| <CopyableCode code="draftPackageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="draft_package_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="edit_package" /> | `text` | field from the `properties` object |
| <CopyableCode code="executable_launch_command" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_party_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="flighting_ring" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="highlighted_files" /> | `text` | field from the `properties` object |
| <CopyableCode code="inplace_upgrade_os_pair" /> | `text` | field from the `properties` object |
| <CopyableCode code="intune_enrollment_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="intune_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="process_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tab_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_os_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="tests" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_autofill" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_sample" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="working_path" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the Test Base Draft Package. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base Draft Package. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the draft packages under a test base account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Creates or replaces a Test Base Draft Package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Draft Package. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Updates an existing Test Base Draft Package. |
| <CopyableCode code="copy_from_package" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName, data__packageId" /> | Copy package file and metadata from a package to this draft package |
| <CopyableCode code="extract_file" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName, data__sourceFile" /> | Performs extracting file operation for a Test Base Draft Package |
| <CopyableCode code="generate_folders_and_scripts" /> | `EXEC` | <CopyableCode code="draftPackageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Generates folders and scripts |

## `SELECT` examples

Lists all the draft packages under a test base account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_draft_packages', value: 'view', },
        { label: 'draft_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
app_file_name,
application_name,
comments,
draftPackageName,
draft_package_path,
edit_package,
executable_launch_command,
first_party_apps,
flighting_ring,
gallery_apps,
highlighted_files,
inplace_upgrade_os_pair,
intune_enrollment_metadata,
intune_metadata,
last_modified_time,
package_id,
package_tags,
process_name,
provisioning_state,
resourceGroupName,
source_type,
subscriptionId,
tab_state,
target_os_list,
testBaseAccountName,
test_types,
tests,
use_autofill,
use_sample,
version,
working_path
FROM azure_extras.test_base.vw_draft_packages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.draft_packages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>draft_packages</code> resource.

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
INSERT INTO azure_extras.test_base.draft_packages (
draftPackageName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties
)
SELECT 
'{{ draftPackageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testBaseAccountName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: applicationName
          value: string
        - name: version
          value: string
        - name: draftPackagePath
          value: string
        - name: workingPath
          value: string
        - name: appFileName
          value: string
        - name: sourceType
          value: []
        - name: useSample
          value: boolean
        - name: comments
          value: string
        - name: intuneMetadata
          value:
            - name: intuneApp
              value:
                - name: appName
                  value: string
                - name: version
                  value: string
                - name: appId
                  value: string
                - name: publisher
                  value: string
                - name: description
                  value: string
                - name: owner
                  value: string
                - name: createDate
                  value: string
                - name: dependentAppCount
                  value: integer
                - name: installCommand
                  value: string
                - name: uninstallCommand
                  value: string
                - name: lastProcessed
                  value: integer
                - name: dependencyIds
                  value:
                    - string
                - name: setupFile
                  value: string
                - name: minimumSupportedOS
                  value: string
                - name: status
                  value: string
                - name: expectedExitCodes
                  value:
                    - string
            - name: intuneAppDependencies
              value:
                - - name: appName
                    value: string
                  - name: version
                    value: string
                  - name: appId
                    value: string
                  - name: publisher
                    value: string
                  - name: description
                    value: string
                  - name: owner
                    value: string
                  - name: createDate
                    value: string
                  - name: dependentAppCount
                    value: integer
                  - name: installCommand
                    value: string
                  - name: uninstallCommand
                    value: string
                  - name: lastProcessed
                    value: integer
                  - name: dependencyIds
                    value:
                      - string
                  - name: setupFile
                    value: string
                  - name: minimumSupportedOS
                    value: string
                  - name: status
                    value: string
                  - name: expectedExitCodes
                    value:
                      - string
        - name: highlightedFiles
          value:
            - - name: path
                value: string
              - name: visited
                value: boolean
              - name: sections
                value:
                  - string
        - name: packageTags
          value: []
        - name: editPackage
          value: boolean
        - name: packageId
          value: string
        - name: useAutofill
          value: boolean
        - name: executableLaunchCommand
          value: string
        - name: processName
          value: string
        - name: tabState
          value:
            - name: currentTab
              value: []
            - name: visitedTabs
              value:
                - []
        - name: testTypes
          value:
            - []
        - name: provisioningState
          value: []
        - name: targetOSList
          value:
            - - name: osUpdateType
                value: string
              - name: targetOSs
                value:
                  - string
              - name: insiderChannelIds
                value:
                  - string
              - name: baselineOSs
                value:
                  - string
              - name: targetOSImageIds
                value:
                  - string
        - name: inplaceUpgradeOSPair
          value:
            - name: baselineOS
              value:
                - name: osName
                  value: string
                - name: customImageId
                  value: string
                - name: customImageDisplayName
                  value: string
                - name: releaseProperties
                  value:
                    - name: releaseName
                      value: string
                    - name: buildNumber
                      value: string
                    - name: buildRevision
                      value: string
                    - name: releaseVersionDate
                      value: string
            - name: targetOS
              value: string
        - name: lastModifiedTime
          value: string
        - name: flightingRing
          value: string
        - name: firstPartyApps
          value:
            - - name: name
                value: string
              - name: architecture
                value: []
              - name: channel
                value: string
              - name: ring
                value: string
              - name: interopExecutionMode
                value: string
        - name: galleryApps
          value:
            - - name: skuId
                value: string
              - name: isConsented
                value: boolean
        - name: tests
          value:
            - - name: testType
                value: []
              - name: validationRunStatus
                value: string
              - name: validationResultId
                value: string
              - name: isActive
                value: boolean
              - name: commands
                value:
                  - - name: name
                      value: string
                    - name: action
                      value: string
                    - name: contentType
                      value: string
                    - name: content
                      value: string
                    - name: runElevated
                      value: boolean
                    - name: restartAfter
                      value: boolean
                    - name: maxRunTime
                      value: integer
                    - name: runAsInteractive
                      value: boolean
                    - name: alwaysRun
                      value: boolean
                    - name: applyUpdateBefore
                      value: boolean
                    - name: install1PAppBefore
                      value: boolean
                    - name: preUpgrade
                      value: boolean
                    - name: postUpgrade
                      value: boolean
                    - name: enrollIntuneBefore
                      value: boolean
        - name: intuneEnrollmentMetadata
          value:
            - name: appList
              value:
                - - name: appName
                    value: string
                  - name: appId
                    value: string
                  - name: expectedInstallationPath
                    value: string
            - name: credentialId
              value: string
            - name: expectedDeploymentDurationInMinute
              value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>draft_packages</code> resource.

```sql
/*+ update */
UPDATE azure_extras.test_base.draft_packages
SET 
properties = '{{ properties }}'
WHERE 
draftPackageName = '{{ draftPackageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```

## `DELETE` example

Deletes the specified <code>draft_packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.draft_packages
WHERE draftPackageName = '{{ draftPackageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
