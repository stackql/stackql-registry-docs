---
title: notes
hide_title: false
hide_table_of_contents: false
keywords:
  - notes
  - containeranalysis
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

Creates, updates, deletes, gets or lists a <code>notes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.containeranalysis.notes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. |
| <CopyableCode code="attestation" /> | `object` | Note kind that represents a logical attestation "role" or "authority". For example, an organization might have one `Authority` for "QA" and one for "build". This note is intended to act strictly as a grouping mechanism for the attached occurrences (Attestations). This grouping mechanism also provides a security boundary, since IAM ACLs gate the ability for a principle to attach an occurrence to a given note. It also provides a single point of lookup to find all attached attestation occurrences, even if they don't all live in the same project. |
| <CopyableCode code="build" /> | `object` | Note holding the version of the provider's builder and the signature of the provenance message in the build details occurrence. |
| <CopyableCode code="compliance" /> | `object` |  |
| <CopyableCode code="createTime" /> | `string` | Output only. The time this note was created. This field can be used as a filter in list requests. |
| <CopyableCode code="deployment" /> | `object` | An artifact that can be deployed in some runtime. |
| <CopyableCode code="discovery" /> | `object` | A note that indicates a type of analysis a provider would perform. This note exists in a provider's project. A `Discovery` occurrence is created in a consumer's project at the start of analysis. |
| <CopyableCode code="dsseAttestation" /> | `object` |  |
| <CopyableCode code="expirationTime" /> | `string` | Time of expiration for this note. Empty if note does not expire. |
| <CopyableCode code="image" /> | `object` | Basis describes the base image portion (Note) of the DockerImage relationship. Linked occurrences are derived from this or an equivalent image via: FROM Or an equivalent reference, e.g., a tag of the resource_url. |
| <CopyableCode code="kind" /> | `string` | Output only. The type of analysis. This field can be used as a filter in list requests. |
| <CopyableCode code="longDescription" /> | `string` | A detailed description of this note. |
| <CopyableCode code="package" /> | `object` | PackageNote represents a particular package version. |
| <CopyableCode code="relatedNoteNames" /> | `array` | Other notes related to this note. |
| <CopyableCode code="relatedUrl" /> | `array` | URLs associated with this note. |
| <CopyableCode code="sbomReference" /> | `object` | The note representing an SBOM reference. |
| <CopyableCode code="shortDescription" /> | `string` | A one sentence description of this note. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time this note was last updated. This field can be used as a filter in list requests. |
| <CopyableCode code="upgrade" /> | `object` | An Upgrade Note represents a potential upgrade of a package to a given version. For each package version combination (i.e. bash 4.0, bash 4.1, bash 4.1.2), there will be an Upgrade Note. For Windows, windows_update field represents the information related to the update. |
| <CopyableCode code="vulnerability" /> | `object` | A security vulnerability that can be found in resources. |
| <CopyableCode code="vulnerabilityAssessment" /> | `object` | A single VulnerabilityAssessmentNote represents one particular product's vulnerability assessment for one CVE. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_notes_get" /> | `SELECT` | <CopyableCode code="locationsId, notesId, projectsId" /> | Gets the specified note. |
| <CopyableCode code="projects_locations_notes_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists notes for the specified project. |
| <CopyableCode code="projects_notes_get" /> | `SELECT` | <CopyableCode code="notesId, projectsId" /> | Gets the specified note. |
| <CopyableCode code="projects_notes_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists notes for the specified project. |
| <CopyableCode code="projects_locations_notes_batch_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates new notes in batch. |
| <CopyableCode code="projects_locations_notes_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new note. |
| <CopyableCode code="projects_notes_batch_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates new notes in batch. |
| <CopyableCode code="projects_notes_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new note. |
| <CopyableCode code="projects_locations_notes_delete" /> | `DELETE` | <CopyableCode code="locationsId, notesId, projectsId" /> | Deletes the specified note. |
| <CopyableCode code="projects_notes_delete" /> | `DELETE` | <CopyableCode code="notesId, projectsId" /> | Deletes the specified note. |
| <CopyableCode code="projects_locations_notes_patch" /> | `UPDATE` | <CopyableCode code="locationsId, notesId, projectsId" /> | Updates the specified note. |
| <CopyableCode code="projects_notes_patch" /> | `UPDATE` | <CopyableCode code="notesId, projectsId" /> | Updates the specified note. |

## `SELECT` examples

Lists notes for the specified project.

```sql
SELECT
name,
attestation,
build,
compliance,
createTime,
deployment,
discovery,
dsseAttestation,
expirationTime,
image,
kind,
longDescription,
package,
relatedNoteNames,
relatedUrl,
sbomReference,
shortDescription,
updateTime,
upgrade,
vulnerability,
vulnerabilityAssessment
FROM google.containeranalysis.notes
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notes</code> resource.

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
INSERT INTO google.containeranalysis.notes (
projectsId,
notes
)
SELECT 
'{{ projectsId }}',
'{{ notes }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
notes: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>notes</code> resource.

```sql
/*+ update */
UPDATE google.containeranalysis.notes
SET 
longDescription = '{{ longDescription }}',
vulnerability = '{{ vulnerability }}',
vulnerabilityAssessment = '{{ vulnerabilityAssessment }}',
discovery = '{{ discovery }}',
dsseAttestation = '{{ dsseAttestation }}',
shortDescription = '{{ shortDescription }}',
build = '{{ build }}',
name = '{{ name }}',
relatedNoteNames = '{{ relatedNoteNames }}',
compliance = '{{ compliance }}',
sbomReference = '{{ sbomReference }}',
package = '{{ package }}',
upgrade = '{{ upgrade }}',
image = '{{ image }}',
attestation = '{{ attestation }}',
deployment = '{{ deployment }}',
relatedUrl = '{{ relatedUrl }}',
expirationTime = '{{ expirationTime }}'
WHERE 
notesId = '{{ notesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>notes</code> resource.

```sql
/*+ delete */
DELETE FROM google.containeranalysis.notes
WHERE notesId = '{{ notesId }}'
AND projectsId = '{{ projectsId }}';
```
