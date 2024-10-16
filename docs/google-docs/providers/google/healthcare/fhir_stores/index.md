---
title: fhir_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_stores
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>fhir_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.fhir_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. Resource name of the FHIR store, of the form `projects/{project_id}/locations/{location}/datasets/{dataset_id}/fhirStores/{fhir_store_id}`. |
| <CopyableCode code="complexDataTypeReferenceParsing" /> | `string` | Enable parsing of references within complex FHIR data types such as Extensions. If this value is set to ENABLED, then features like referential integrity and Bundle reference rewriting apply to all references. If this flag has not been specified the behavior of the FHIR store will not change, references in complex data types will not be parsed. New stores will have this value set to ENABLED after a notification period. Warning: turning on this flag causes processing existing resources to fail if they contain references to non-existent resources. |
| <CopyableCode code="defaultSearchHandlingStrict" /> | `boolean` | If true, overrides the default search behavior for this FHIR store to `handling=strict` which returns an error for unrecognized search parameters. If false, uses the FHIR specification default `handling=lenient` which ignores unrecognized search parameters. The handling can always be changed from the default on an individual API call by setting the HTTP header `Prefer: handling=strict` or `Prefer: handling=lenient`. Defaults to false. |
| <CopyableCode code="disableReferentialIntegrity" /> | `boolean` | Immutable. Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store creation. The default value is false, meaning that the API enforces referential integrity and fails the requests that result in inconsistent state in the FHIR store. When this field is set to true, the API skips referential integrity checks. Consequently, operations that rely on references, such as GetPatientEverything, do not return all the results if broken references exist. |
| <CopyableCode code="disableResourceVersioning" /> | `boolean` | Immutable. Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation of FHIR store. If set to false, all write operations cause historical versions to be recorded automatically. The historical versions can be fetched through the history APIs, but cannot be updated. If set to true, no historical versions are kept. The server sends errors for attempts to read the historical versions. Defaults to false. |
| <CopyableCode code="enableUpdateCreate" /> | `boolean` | Whether this FHIR store has the [updateCreate capability](https://www.hl7.org/fhir/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate). This determines if the client can use an Update operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through the Create operation and attempts to update a non-existent resource return errors. It is strongly advised not to include or encode any sensitive data such as patient identifiers in client-specified resource IDs. Those IDs are part of the FHIR resource path recorded in Cloud audit logs and Pub/Sub notifications. Those IDs can also be contained in reference fields within other resources. Defaults to false. |
| <CopyableCode code="labels" /> | `object` | User-supplied key-value pairs used to organize FHIR stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| <CopyableCode code="notificationConfig" /> | `object` | Specifies where to send notifications upon changes to a data store. |
| <CopyableCode code="notificationConfigs" /> | `array` | Specifies where and whether to send notifications upon changes to a FHIR store. |
| <CopyableCode code="streamConfigs" /> | `array` | A list of streaming configs that configure the destinations of streaming export for every resource mutation in this FHIR store. Each store is allowed to have up to 10 streaming configs. After a new config is added, the next resource mutation is streamed to the new location in addition to the existing ones. When a location is removed from the list, the server stops streaming to that location. Before adding a new config, you must add the required [`bigquery.dataEditor`](https://cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) role to your project's **Cloud Healthcare Service Agent** [service account](https://cloud.google.com/iam/docs/service-accounts). Some lag (typically on the order of dozens of seconds) is expected before the results show up in the streaming destination. |
| <CopyableCode code="validationConfig" /> | `object` | Contains the configuration for FHIR profiles and validation. |
| <CopyableCode code="version" /> | `string` | Required. Immutable. The FHIR specification version that this FHIR store supports natively. This field is immutable after store creation. Requests are rejected if they contain FHIR resources of a different version. Version is required for every FHIR store. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Gets the configuration of the specified FHIR store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists the FHIR stores in the given dataset. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Creates a new FHIR store within the parent dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Deletes the specified FHIR store and removes all resources within it. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Updates the configuration of the specified FHIR store. |
| <CopyableCode code="deidentify" /> | `EXEC` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | De-identifies data from the source store and writes it to the destination store. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifyFhirStoreSummary. If errors occur, error is set. Error details are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Export resources from the FHIR store to the specified destination. This method returns an Operation that can be used to track the status of the export by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a detailed response of type ExportResourcesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Imports resources to the FHIR store by loading data from the specified sources. This method is optimized to load large quantities of data using import semantics that ignore some FHIR store configuration options and are not suitable for all use cases. It is primarily intended to load data into an empty FHIR store that is not being used by other clients. In cases where this method is not appropriate, consider using ExecuteBundle to load data. Every resource in the input must contain a client-supplied ID. Each resource is stored using the supplied ID regardless of the enable_update_create setting on the FHIR store. It is strongly advised not to include or encode any sensitive data such as patient identifiers in client-specified resource IDs. Those IDs are part of the FHIR resource path recorded in Cloud Audit Logs and Cloud Pub/Sub notifications. Those IDs can also be contained in reference fields within other resources. The import process does not enforce referential integrity, regardless of the disable_referential_integrity setting on the FHIR store. This allows the import of resources with arbitrary interdependencies without considering grouping or ordering, but if the input data contains invalid references or if some resources fail to be imported, the FHIR store might be left in a state that violates referential integrity. The import process does not trigger Pub/Sub notification or BigQuery streaming update, regardless of how those are configured on the FHIR store. If a resource with the specified ID already exists, the most recent version of the resource is overwritten without creating a new historical version, regardless of the disable_resource_versioning setting on the FHIR store. If transient failures occur during the import, it's possible that successfully imported resources will be overwritten more than once. The import operation is idempotent unless the input data contains multiple valid resources with the same ID but different contents. In that case, after the import completes, the store contains exactly one resource with that ID but there is no ordering guarantee on which version of the contents it will have. The operation result counters do not count duplicate IDs as an error and count one success for each resource in the input, which might result in a success count larger than the number of resources in the FHIR store. This often occurs when importing data organized in bundles produced by Patient-everything where each bundle contains its own copy of a resource such as Practitioner that might be referred to by many patients. If some resources fail to import, for example due to parsing errors, successfully imported resources are not rolled back. The location and format of the input data is specified by the parameters in ImportResourcesRequest. Note that if no format is specified, this method assumes the `BUNDLE` format. When using the `BUNDLE` format this method ignores the `Bundle.type` field, except that `history` bundles are rejected, and does not apply any of the bundle processing semantics for batch or transaction bundles. Unlike in ExecuteBundle, transaction bundles are not executed as a single transaction and bundle-internal references are not rewritten. The bundle is treated as a collection of resources to be written as provided in `Bundle.entry.resource`, ignoring `Bundle.entry.request`. As an example, this allows the import of `searchset` bundles produced by a FHIR search or Patient-everything operation. This method returns an Operation that can be used to track the status of the import by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a detailed response of type ImportResourcesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Rolls back resources from the FHIR store to the specified time. This method returns an Operation that can be used to track the status of the rollback by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a detailed response of type RollbackFhirResourcesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |

## `SELECT` examples

Lists the FHIR stores in the given dataset.

```sql
SELECT
name,
complexDataTypeReferenceParsing,
defaultSearchHandlingStrict,
disableReferentialIntegrity,
disableResourceVersioning,
enableUpdateCreate,
labels,
notificationConfig,
notificationConfigs,
streamConfigs,
validationConfig,
version
FROM google.healthcare.fhir_stores
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fhir_stores</code> resource.

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
INSERT INTO google.healthcare.fhir_stores (
datasetsId,
locationsId,
projectsId,
name,
enableUpdateCreate,
notificationConfig,
disableReferentialIntegrity,
disableResourceVersioning,
labels,
version,
streamConfigs,
validationConfig,
defaultSearchHandlingStrict,
complexDataTypeReferenceParsing,
notificationConfigs
)
SELECT 
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
{{ enableUpdateCreate }},
'{{ notificationConfig }}',
{{ disableReferentialIntegrity }},
{{ disableResourceVersioning }},
'{{ labels }}',
'{{ version }}',
'{{ streamConfigs }}',
'{{ validationConfig }}',
{{ defaultSearchHandlingStrict }},
'{{ complexDataTypeReferenceParsing }}',
'{{ notificationConfigs }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: enableUpdateCreate
      value: boolean
    - name: notificationConfig
      value:
        - name: pubsubTopic
          value: string
        - name: sendForBulkImport
          value: boolean
    - name: disableReferentialIntegrity
      value: boolean
    - name: disableResourceVersioning
      value: boolean
    - name: labels
      value: object
    - name: version
      value: string
    - name: streamConfigs
      value:
        - - name: resourceTypes
            value:
              - string
          - name: bigqueryDestination
            value:
              - name: datasetUri
                value: string
              - name: schemaConfig
                value:
                  - name: schemaType
                    value: string
                  - name: recursiveStructureDepth
                    value: string
                  - name: lastUpdatedPartitionConfig
                    value:
                      - name: type
                        value: string
                      - name: expirationMs
                        value: string
              - name: force
                value: boolean
              - name: writeDisposition
                value: string
          - name: deidentifiedStoreDestination
            value:
              - name: store
                value: string
              - name: config
                value:
                  - name: dicom
                    value:
                      - name: skipIdRedaction
                        value: boolean
                      - name: keepList
                        value:
                          - name: tags
                            value:
                              - string
                      - name: filterProfile
                        value: string
                  - name: fhir
                    value:
                      - name: fieldMetadataList
                        value:
                          - - name: paths
                              value:
                                - string
                            - name: action
                              value: string
                      - name: defaultKeepExtensions
                        value: boolean
                  - name: image
                    value:
                      - name: textRedactionMode
                        value: string
                  - name: text
                    value:
                      - name: transformations
                        value:
                          - - name: infoTypes
                              value:
                                - string
                            - name: redactConfig
                              value: []
                            - name: characterMaskConfig
                              value:
                                - name: maskingCharacter
                                  value: string
                            - name: dateShiftConfig
                              value:
                                - name: cryptoKey
                                  value: string
                                - name: kmsWrapped
                                  value:
                                    - name: wrappedKey
                                      value: string
                                    - name: cryptoKey
                                      value: string
                            - name: cryptoHashConfig
                              value:
                                - name: cryptoKey
                                  value: string
                            - name: replaceWithInfoTypeConfig
                              value: []
                      - name: additionalTransformations
                        value:
                          - - name: infoTypes
                              value:
                                - string
                      - name: excludeInfoTypes
                        value:
                          - string
                  - name: useRegionalDataProcessing
                    value: boolean
    - name: validationConfig
      value:
        - name: disableProfileValidation
          value: boolean
        - name: enabledImplementationGuides
          value:
            - string
        - name: disableRequiredFieldValidation
          value: boolean
        - name: disableReferenceTypeValidation
          value: boolean
        - name: disableFhirpathValidation
          value: boolean
    - name: defaultSearchHandlingStrict
      value: boolean
    - name: complexDataTypeReferenceParsing
      value: string
    - name: notificationConfigs
      value:
        - - name: pubsubTopic
            value: string
          - name: sendFullResource
            value: boolean
          - name: sendPreviousResourceOnDelete
            value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>fhir_stores</code> resource.

```sql
/*+ update */
UPDATE google.healthcare.fhir_stores
SET 
name = '{{ name }}',
enableUpdateCreate = true|false,
notificationConfig = '{{ notificationConfig }}',
disableReferentialIntegrity = true|false,
disableResourceVersioning = true|false,
labels = '{{ labels }}',
version = '{{ version }}',
streamConfigs = '{{ streamConfigs }}',
validationConfig = '{{ validationConfig }}',
defaultSearchHandlingStrict = true|false,
complexDataTypeReferenceParsing = '{{ complexDataTypeReferenceParsing }}',
notificationConfigs = '{{ notificationConfigs }}'
WHERE 
datasetsId = '{{ datasetsId }}'
AND fhirStoresId = '{{ fhirStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>fhir_stores</code> resource.

```sql
/*+ delete */
DELETE FROM google.healthcare.fhir_stores
WHERE datasetsId = '{{ datasetsId }}'
AND fhirStoresId = '{{ fhirStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
