---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - binaryauthorization
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.binaryauthorization.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the Binary Authorization platform policy, in the form of `projects/*/platforms/*/policies/*`. |
| <CopyableCode code="description" /> | `string` | Optional. A description comment about the policy. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to prevent updating the policy when another request has updated it since it was retrieved. |
| <CopyableCode code="gkePolicy" /> | `object` | A Binary Authorization policy for a GKE cluster. This is one type of policy that can occur as a `PlatformPolicy`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the policy was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="platformsId, policiesId, projectsId" /> | Gets a platform policy. Returns `NOT_FOUND` if the policy doesn't exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="platformsId, projectsId" /> | Lists platform policies owned by a project in the specified platform. Returns `INVALID_ARGUMENT` if the project or the platform doesn't exist. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="platformsId, projectsId" /> | Creates a platform policy, and returns a copy of it. Returns `NOT_FOUND` if the project or platform doesn't exist, `INVALID_ARGUMENT` if the request is malformed, `ALREADY_EXISTS` if the policy already exists, and `INVALID_ARGUMENT` if the policy contains a platform-specific policy that does not match the platform value specified in the URL. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="platformsId, policiesId, projectsId" /> | Deletes a platform policy. Returns `NOT_FOUND` if the policy doesn't exist. |
| <CopyableCode code="replace_platform_policy" /> | `REPLACE` | <CopyableCode code="platformsId, policiesId, projectsId" /> | Replaces a platform policy. Returns `NOT_FOUND` if the policy doesn't exist. |
| <CopyableCode code="evaluate" /> | `EXEC` | <CopyableCode code="policiesId, projectsId" /> | Evaluates a Kubernetes object versus a GKE platform policy. Returns `NOT_FOUND` if the policy doesn't exist, `INVALID_ARGUMENT` if the policy or request is malformed and `PERMISSION_DENIED` if the client does not have sufficient permissions. |

## `SELECT` examples

Lists platform policies owned by a project in the specified platform. Returns `INVALID_ARGUMENT` if the project or the platform doesn't exist.

```sql
SELECT
name,
description,
etag,
gkePolicy,
updateTime
FROM google.binaryauthorization.policies
WHERE platformsId = '{{ platformsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO google.binaryauthorization.policies (
platformsId,
projectsId,
description,
gkePolicy,
etag
)
SELECT 
'{{ platformsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ gkePolicy }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: gkePolicy
      value:
        - name: imageAllowlist
          value:
            - name: allowPattern
              value:
                - string
        - name: checkSets
          value:
            - - name: displayName
                value: string
              - name: scope
                value:
                  - name: kubernetesServiceAccount
                    value: string
                  - name: kubernetesNamespace
                    value: string
              - name: checks
                value:
                  - - name: displayName
                      value: string
                    - name: alwaysDeny
                      value: boolean
                    - name: simpleSigningAttestationCheck
                      value:
                        - name: attestationAuthenticators
                          value:
                            - - name: displayName
                                value: string
                              - name: pkixPublicKeySet
                                value:
                                  - name: pkixPublicKeys
                                    value:
                                      - - name: publicKeyPem
                                          value: string
                                        - name: signatureAlgorithm
                                          value: string
                                        - name: keyId
                                          value: string
                        - name: containerAnalysisAttestationProjects
                          value:
                            - string
                    - name: trustedDirectoryCheck
                      value:
                        - name: trustedDirPatterns
                          value:
                            - string
                    - name: imageFreshnessCheck
                      value:
                        - name: maxUploadAgeDays
                          value: integer
                    - name: vulnerabilityCheck
                      value:
                        - name: allowedCves
                          value:
                            - string
                        - name: blockedCves
                          value:
                            - string
                        - name: maximumUnfixableSeverity
                          value: string
                        - name: maximumFixableSeverity
                          value: string
                        - name: containerAnalysisVulnerabilityProjects
                          value:
                            - string
                    - name: slsaCheck
                      value:
                        - name: rules
                          value:
                            - - name: trustedBuilder
                                value: string
                              - name: attestationSource
                                value:
                                  - name: containerAnalysisAttestationProjects
                                    value:
                                      - string
                              - name: configBasedBuildRequired
                                value: boolean
                              - name: trustedSourceRepoPatterns
                                value:
                                  - string
                    - name: sigstoreSignatureCheck
                      value:
                        - name: sigstoreAuthorities
                          value:
                            - - name: displayName
                                value: string
                              - name: publicKeySet
                                value:
                                  - name: publicKeys
                                    value:
                                      - - name: publicKeyPem
                                          value: string
    - name: updateTime
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>policies</code> resource.

```sql
/*+ update */
REPLACE google.binaryauthorization.policies
SET 
description = '{{ description }}',
gkePolicy = '{{ gkePolicy }}',
etag = '{{ etag }}'
WHERE 
platformsId = '{{ platformsId }}'
AND policiesId = '{{ policiesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.binaryauthorization.policies
WHERE platformsId = '{{ platformsId }}'
AND policiesId = '{{ policiesId }}'
AND projectsId = '{{ projectsId }}';
```
