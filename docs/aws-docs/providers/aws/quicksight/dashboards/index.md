---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>dashboard</code> resource or lists <code>dashboards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Dashboard Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.dashboards" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that this dashboard was created.</p></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td><p>A list of Amazon QuickSight parameters and the list's override values.</p></td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_entity" /></td><td><code>object</code></td><td><p>Dashboard source entity.</p></td></tr>
<tr><td><CopyableCode code="theme_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The last time that this dashboard was updated.</p></td></tr>
<tr><td><CopyableCode code="validation_strategy" /></td><td><code>object</code></td><td><p>The option to relax the validation that is required to create and update analyses, dashboards, and templates with definition objects. When you set this value to <code>LENIENT</code>, validation is skipped for specific errors.</p></td></tr>
<tr><td><CopyableCode code="folder_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="link_sharing_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dashboard_publish_options" /></td><td><code>object</code></td><td><p>Dashboard publish options.</p></td></tr>
<tr><td><CopyableCode code="last_published_time" /></td><td><code>string</code></td><td><p>The last time that this dashboard was published.</p></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>object</code></td><td><p>Dashboard version.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="link_entities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the resource.</p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html"><code>AWS::QuickSight::Dashboard</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AwsAccountId, DashboardId, Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>dashboards</code> in a region.
```sql
SELECT
region,
created_time,
parameters,
version_description,
source_entity,
theme_arn,
definition,
last_updated_time,
validation_strategy,
folder_arns,
dashboard_id,
link_sharing_configuration,
name,
dashboard_publish_options,
last_published_time,
version,
aws_account_id,
permissions,
link_entities,
arn,
tags
FROM aws.quicksight.dashboards
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dashboard</code>.
```sql
SELECT
region,
created_time,
parameters,
version_description,
source_entity,
theme_arn,
definition,
last_updated_time,
validation_strategy,
folder_arns,
dashboard_id,
link_sharing_configuration,
name,
dashboard_publish_options,
last_published_time,
version,
aws_account_id,
permissions,
link_entities,
arn,
tags
FROM aws.quicksight.dashboards
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<DashboardId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dashboard</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.quicksight.dashboards (
 DashboardId,
 Name,
 AwsAccountId,
 region
)
SELECT 
'{{ DashboardId }}',
 '{{ Name }}',
 '{{ AwsAccountId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.dashboards (
 Parameters,
 VersionDescription,
 SourceEntity,
 ThemeArn,
 Definition,
 ValidationStrategy,
 FolderArns,
 DashboardId,
 LinkSharingConfiguration,
 Name,
 DashboardPublishOptions,
 AwsAccountId,
 Permissions,
 LinkEntities,
 Tags,
 region
)
SELECT 
 '{{ Parameters }}',
 '{{ VersionDescription }}',
 '{{ SourceEntity }}',
 '{{ ThemeArn }}',
 '{{ Definition }}',
 '{{ ValidationStrategy }}',
 '{{ FolderArns }}',
 '{{ DashboardId }}',
 '{{ LinkSharingConfiguration }}',
 '{{ Name }}',
 '{{ DashboardPublishOptions }}',
 '{{ AwsAccountId }}',
 '{{ Permissions }}',
 '{{ LinkEntities }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: dashboard
    props:
      - name: Parameters
        value:
          StringParameters:
            - Values:
                - '{{ Values[0] }}'
              Name: '{{ Name }}'
          DecimalParameters:
            - Values:
                - null
              Name: '{{ Name }}'
          IntegerParameters:
            - Values:
                - null
              Name: '{{ Name }}'
          DateTimeParameters:
            - Values:
                - '{{ Values[0] }}'
              Name: '{{ Name }}'
      - name: VersionDescription
        value: '{{ VersionDescription }}'
      - name: SourceEntity
        value:
          SourceTemplate:
            DataSetReferences:
              - DataSetArn: '{{ DataSetArn }}'
                DataSetPlaceholder: '{{ DataSetPlaceholder }}'
            Arn: '{{ Arn }}'
      - name: ThemeArn
        value: '{{ ThemeArn }}'
      - name: Definition
        value:
          Options:
            Timezone: '{{ Timezone }}'
            WeekStart: '{{ WeekStart }}'
          FilterGroups:
            - Status: '{{ Status }}'
              Filters:
                - NestedFilter:
                    Column:
                      ColumnName: '{{ ColumnName }}'
                      DataSetIdentifier: '{{ DataSetIdentifier }}'
                    InnerFilter:
                      CategoryInnerFilter:
                        Configuration:
                          CustomFilterListConfiguration:
                            CategoryValues:
                              - '{{ CategoryValues[0] }}'
                            NullOption: '{{ NullOption }}'
                            MatchOperator: '{{ MatchOperator }}'
                            SelectAllOptions: '{{ SelectAllOptions }}'
                          CustomFilterConfiguration:
                            CategoryValue: '{{ CategoryValue }}'
                            ParameterName: '{{ ParameterName }}'
                            NullOption: null
                            MatchOperator: null
                            SelectAllOptions: null
                          FilterListConfiguration:
                            CategoryValues:
                              - '{{ CategoryValues[0] }}'
                            NullOption: null
                            MatchOperator: null
                            SelectAllOptions: null
                        Column: null
                        DefaultFilterControlConfiguration:
                          ControlOptions:
                            DefaultSliderOptions:
                              Type: '{{ Type }}'
                              StepSize: null
                              DisplayOptions:
                                TitleOptions:
                                  CustomLabel: '{{ CustomLabel }}'
                                  Visibility: null
                                  FontConfiguration:
                                    FontStyle: '{{ FontStyle }}'
                                    FontSize:
                                      Relative: '{{ Relative }}'
                                    FontDecoration: '{{ FontDecoration }}'
                                    FontColor: '{{ FontColor }}'
                                    FontWeight:
                                      Name: '{{ Name }}'
                                InfoIconLabelOptions:
                                  Visibility: null
                                  InfoIconText: '{{ InfoIconText }}'
                              MaximumValue: null
                              MinimumValue: null
                            DefaultRelativeDateTimeOptions:
                              DisplayOptions:
                                TitleOptions: null
                                InfoIconLabelOptions: null
                                DateTimeFormat: '{{ DateTimeFormat }}'
                              CommitMode: '{{ CommitMode }}'
                            DefaultTextFieldOptions:
                              DisplayOptions:
                                TitleOptions: null
                                PlaceholderOptions:
                                  Visibility: null
                                InfoIconLabelOptions: null
                            DefaultTextAreaOptions:
                              Delimiter: '{{ Delimiter }}'
                              DisplayOptions:
                                TitleOptions: null
                                PlaceholderOptions: null
                                InfoIconLabelOptions: null
                            DefaultDropdownOptions:
                              Type: '{{ Type }}'
                              DisplayOptions:
                                TitleOptions: null
                                SelectAllOptions:
                                  Visibility: null
                                InfoIconLabelOptions: null
                              CommitMode: null
                              SelectableValues:
                                Values:
                                  - '{{ Values[0] }}'
                            DefaultDateTimePickerOptions:
                              Type: '{{ Type }}'
                              DisplayOptions:
                                TitleOptions: null
                                InfoIconLabelOptions: null
                                DateTimeFormat: '{{ DateTimeFormat }}'
                              CommitMode: null
                            DefaultListOptions:
                              Type: null
                              DisplayOptions:
                                TitleOptions: null
                                SearchOptions:
                                  Visibility: null
                                SelectAllOptions: null
                                InfoIconLabelOptions: null
                              SelectableValues: null
                          Title: '{{ Title }}'
                    IncludeInnerSet: '{{ IncludeInnerSet }}'
                    FilterId: '{{ FilterId }}'
                  NumericEqualityFilter:
                    AggregationFunction:
                      AttributeAggregationFunction:
                        SimpleAttributeAggregation: '{{ SimpleAttributeAggregation }}'
                        ValueForMultipleValues: '{{ ValueForMultipleValues }}'
                      DateAggregationFunction: '{{ DateAggregationFunction }}'
                      NumericalAggregationFunction:
                        PercentileAggregation:
                          PercentileValue: null
                        SimpleNumericalAggregation: '{{ SimpleNumericalAggregation }}'
                      CategoricalAggregationFunction: '{{ CategoricalAggregationFunction }}'
                    Column: null
                    Value: null
                    ParameterName: '{{ ParameterName }}'
                    NullOption: null
                    MatchOperator: '{{ MatchOperator }}'
                    SelectAllOptions: '{{ SelectAllOptions }}'
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
                  NumericRangeFilter:
                    AggregationFunction: null
                    Column: null
                    IncludeMaximum: '{{ IncludeMaximum }}'
                    RangeMinimum:
                      StaticValue: null
                      Parameter: '{{ Parameter }}'
                    NullOption: null
                    SelectAllOptions: null
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
                    RangeMaximum: null
                    IncludeMinimum: '{{ IncludeMinimum }}'
                  TimeRangeFilter:
                    RangeMinimumValue:
                      RollingDate:
                        Expression: '{{ Expression }}'
                        DataSetIdentifier: '{{ DataSetIdentifier }}'
                      StaticValue: '{{ StaticValue }}'
                      Parameter: '{{ Parameter }}'
                    Column: null
                    RangeMaximumValue: null
                    IncludeMaximum: '{{ IncludeMaximum }}'
                    TimeGranularity: '{{ TimeGranularity }}'
                    NullOption: null
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
                    IncludeMinimum: '{{ IncludeMinimum }}'
                    ExcludePeriodConfiguration:
                      Status: null
                      Amount: null
                      Granularity: null
                  RelativeDatesFilter:
                    RelativeDateValue: null
                    Column: null
                    RelativeDateType: '{{ RelativeDateType }}'
                    TimeGranularity: null
                    ParameterName: '{{ ParameterName }}'
                    NullOption: null
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
                    AnchorDateConfiguration:
                      AnchorOption: '{{ AnchorOption }}'
                      ParameterName: '{{ ParameterName }}'
                    MinimumGranularity: null
                    ExcludePeriodConfiguration: null
                  TopBottomFilter:
                    AggregationSortConfigurations:
                      - AggregationFunction: null
                        SortDirection: '{{ SortDirection }}'
                        Column: null
                    Column: null
                    TimeGranularity: null
                    ParameterName: '{{ ParameterName }}'
                    Limit: null
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
                  TimeEqualityFilter:
                    Column: null
                    RollingDate: null
                    Value: '{{ Value }}'
                    TimeGranularity: null
                    ParameterName: '{{ ParameterName }}'
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
                  CategoryFilter:
                    Configuration: null
                    Column: null
                    DefaultFilterControlConfiguration: null
                    FilterId: '{{ FilterId }}'
              CrossDataset: '{{ CrossDataset }}'
              ScopeConfiguration:
                AllSheets: {}
                SelectedSheets:
                  SheetVisualScopingConfigurations:
                    - Scope: '{{ Scope }}'
                      SheetId: '{{ SheetId }}'
                      VisualIds:
                        - '{{ VisualIds[0] }}'
              FilterGroupId: '{{ FilterGroupId }}'
          StaticFiles:
            - ImageStaticFile:
                StaticFileId: '{{ StaticFileId }}'
                Source:
                  UrlOptions:
                    Url: '{{ Url }}'
                  S3Options:
                    BucketName: '{{ BucketName }}'
                    ObjectKey: '{{ ObjectKey }}'
                    Region: '{{ Region }}'
              SpatialStaticFile:
                StaticFileId: '{{ StaticFileId }}'
                Source: null
          CalculatedFields:
            - Expression: '{{ Expression }}'
              DataSetIdentifier: '{{ DataSetIdentifier }}'
              Name: '{{ Name }}'
          DataSetIdentifierDeclarations:
            - Identifier: '{{ Identifier }}'
              DataSetArn: '{{ DataSetArn }}'
          ColumnConfigurations:
            - Role: '{{ Role }}'
              FormatConfiguration:
                NumberFormatConfiguration:
                  FormatConfiguration:
                    NumberDisplayFormatConfiguration:
                      NegativeValueConfiguration:
                        DisplayMode: '{{ DisplayMode }}'
                      DecimalPlacesConfiguration:
                        DecimalPlaces: null
                      NumberScale: '{{ NumberScale }}'
                      NullValueFormatConfiguration:
                        NullString: '{{ NullString }}'
                      Suffix: '{{ Suffix }}'
                      SeparatorConfiguration:
                        DecimalSeparator: '{{ DecimalSeparator }}'
                        ThousandsSeparator:
                          Symbol: null
                          Visibility: null
                      Prefix: '{{ Prefix }}'
                    CurrencyDisplayFormatConfiguration:
                      NegativeValueConfiguration: null
                      DecimalPlacesConfiguration: null
                      NumberScale: null
                      NullValueFormatConfiguration: null
                      Suffix: '{{ Suffix }}'
                      SeparatorConfiguration: null
                      Symbol: '{{ Symbol }}'
                      Prefix: '{{ Prefix }}'
                    PercentageDisplayFormatConfiguration:
                      NegativeValueConfiguration: null
                      DecimalPlacesConfiguration: null
                      NullValueFormatConfiguration: null
                      Suffix: '{{ Suffix }}'
                      SeparatorConfiguration: null
                      Prefix: '{{ Prefix }}'
                DateTimeFormatConfiguration:
                  NumericFormatConfiguration: null
                  NullValueFormatConfiguration: null
                  DateTimeFormat: '{{ DateTimeFormat }}'
                StringFormatConfiguration:
                  NumericFormatConfiguration: null
                  NullValueFormatConfiguration: null
              Column: null
              ColorsConfiguration:
                CustomColors:
                  - Color: '{{ Color }}'
                    FieldValue: '{{ FieldValue }}'
                    SpecialValue: '{{ SpecialValue }}'
          AnalysisDefaults:
            DefaultNewSheetConfiguration:
              SheetContentType: '{{ SheetContentType }}'
              InteractiveLayoutConfiguration:
                FreeForm:
                  CanvasSizeOptions:
                    ScreenCanvasSizeOptions:
                      OptimizedViewPortWidth: '{{ OptimizedViewPortWidth }}'
                Grid:
                  CanvasSizeOptions:
                    ScreenCanvasSizeOptions:
                      OptimizedViewPortWidth: '{{ OptimizedViewPortWidth }}'
                      ResizeOption: '{{ ResizeOption }}'
              PaginatedLayoutConfiguration:
                SectionBased:
                  CanvasSizeOptions:
                    PaperCanvasSizeOptions:
                      PaperMargin:
                        Left: '{{ Left }}'
                        Top: '{{ Top }}'
                        Right: '{{ Right }}'
                        Bottom: '{{ Bottom }}'
                      PaperSize: '{{ PaperSize }}'
                      PaperOrientation: '{{ PaperOrientation }}'
          Sheets:
            - Description: '{{ Description }}'
              ParameterControls:
                - Slider:
                    ParameterControlId: '{{ ParameterControlId }}'
                    StepSize: null
                    DisplayOptions: null
                    SourceParameterName: '{{ SourceParameterName }}'
                    Title: '{{ Title }}'
                    MaximumValue: null
                    MinimumValue: null
                  TextArea:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Delimiter: '{{ Delimiter }}'
                    DisplayOptions: null
                    SourceParameterName: '{{ SourceParameterName }}'
                    Title: '{{ Title }}'
                  Dropdown:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Type: null
                    DisplayOptions: null
                    SourceParameterName: '{{ SourceParameterName }}'
                    CascadingControlConfiguration:
                      SourceControls:
                        - SourceSheetControlId: '{{ SourceSheetControlId }}'
                          ColumnToMatch: null
                    Title: '{{ Title }}'
                    CommitMode: null
                    SelectableValues:
                      LinkToDataSetColumn: null
                      Values:
                        - '{{ Values[0] }}'
                  TextField:
                    ParameterControlId: '{{ ParameterControlId }}'
                    DisplayOptions: null
                    SourceParameterName: '{{ SourceParameterName }}'
                    Title: '{{ Title }}'
                  List:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Type: null
                    DisplayOptions: null
                    SourceParameterName: '{{ SourceParameterName }}'
                    CascadingControlConfiguration: null
                    Title: '{{ Title }}'
                    SelectableValues: null
                  DateTimePicker:
                    ParameterControlId: '{{ ParameterControlId }}'
                    DisplayOptions: null
                    SourceParameterName: '{{ SourceParameterName }}'
                    Title: '{{ Title }}'
              TextBoxes:
                - SheetTextBoxId: '{{ SheetTextBoxId }}'
                  Content: '{{ Content }}'
              Layouts:
                - Configuration:
                    GridLayout:
                      CanvasSizeOptions: null
                      Elements:
                        - ElementType: '{{ ElementType }}'
                          ColumnSpan: null
                          ColumnIndex: null
                          RowIndex: null
                          RowSpan: null
                          ElementId: '{{ ElementId }}'
                    FreeFormLayout:
                      CanvasSizeOptions: null
                      Elements:
                        - ElementType: null
                          BorderStyle:
                            Color: '{{ Color }}'
                            Visibility: null
                          Height: '{{ Height }}'
                          Visibility: null
                          RenderingRules:
                            - Expression: '{{ Expression }}'
                              ConfigurationOverrides:
                                Visibility: null
                          YAxisLocation: '{{ YAxisLocation }}'
                          LoadingAnimation:
                            Visibility: null
                          Width: '{{ Width }}'
                          BackgroundStyle:
                            Color: '{{ Color }}'
                            Visibility: null
                          ElementId: '{{ ElementId }}'
                          XAxisLocation: '{{ XAxisLocation }}'
                          SelectedBorderStyle: null
                    SectionBasedLayout:
                      CanvasSizeOptions: null
                      FooterSections:
                        - Layout:
                            FreeFormLayout:
                              Elements:
                                - null
                          Style:
                            Padding: null
                            Height: '{{ Height }}'
                          SectionId: '{{ SectionId }}'
                      BodySections:
                        - Content:
                            Layout: null
                          Style: null
                          PageBreakConfiguration:
                            After:
                              Status: '{{ Status }}'
                          SectionId: '{{ SectionId }}'
                      HeaderSections:
                        - null
              ContentType: null
              SheetId: '{{ SheetId }}'
              FilterControls:
                - Slider:
                    FilterControlId: '{{ FilterControlId }}'
                    Type: null
                    StepSize: null
                    DisplayOptions: null
                    Title: '{{ Title }}'
                    MaximumValue: null
                    SourceFilterId: '{{ SourceFilterId }}'
                    MinimumValue: null
                  TextArea:
                    FilterControlId: '{{ FilterControlId }}'
                    Delimiter: '{{ Delimiter }}'
                    DisplayOptions: null
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                  Dropdown:
                    FilterControlId: '{{ FilterControlId }}'
                    Type: null
                    DisplayOptions: null
                    CascadingControlConfiguration: null
                    Title: '{{ Title }}'
                    CommitMode: null
                    SourceFilterId: '{{ SourceFilterId }}'
                    SelectableValues: null
                  TextField:
                    FilterControlId: '{{ FilterControlId }}'
                    DisplayOptions: null
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                  List:
                    FilterControlId: '{{ FilterControlId }}'
                    Type: null
                    DisplayOptions: null
                    CascadingControlConfiguration: null
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    SelectableValues: null
                  DateTimePicker:
                    FilterControlId: '{{ FilterControlId }}'
                    Type: null
                    DisplayOptions: null
                    Title: '{{ Title }}'
                    CommitMode: null
                    SourceFilterId: '{{ SourceFilterId }}'
                  RelativeDateTime:
                    FilterControlId: '{{ FilterControlId }}'
                    DisplayOptions: null
                    Title: '{{ Title }}'
                    CommitMode: null
                    SourceFilterId: '{{ SourceFilterId }}'
                  CrossSheet:
                    FilterControlId: '{{ FilterControlId }}'
                    CascadingControlConfiguration: null
                    SourceFilterId: '{{ SourceFilterId }}'
              Images:
                - Actions:
                    - Status: null
                      Trigger: '{{ Trigger }}'
                      CustomActionId: '{{ CustomActionId }}'
                      Name: '{{ Name }}'
                      ActionOperations:
                        - NavigationOperation:
                            LocalNavigationConfiguration:
                              TargetSheetId: '{{ TargetSheetId }}'
                          SetParametersOperation:
                            ParameterValueConfigurations:
                              - DestinationParameterName: '{{ DestinationParameterName }}'
                                Value:
                                  CustomValuesConfiguration:
                                    IncludeNullValue: '{{ IncludeNullValue }}'
                                    CustomValues:
                                      DecimalValues:
                                        - null
                                      IntegerValues:
                                        - null
                                      StringValues:
                                        - '{{ StringValues[0] }}'
                                      DateTimeValues:
                                        - '{{ DateTimeValues[0] }}'
                                  SourceParameterName: '{{ SourceParameterName }}'
                                  SelectAllValueOptions: '{{ SelectAllValueOptions }}'
                                  SourceField: '{{ SourceField }}'
                                  SourceColumn: null
                          URLOperation:
                            URLTemplate: '{{ URLTemplate }}'
                            URLTarget: '{{ URLTarget }}'
                  SheetImageId: '{{ SheetImageId }}'
                  Tooltip:
                    Visibility: null
                    TooltipText:
                      PlainText: '{{ PlainText }}'
                  Scaling:
                    ScalingType: '{{ ScalingType }}'
                  Interactions:
                    ImageMenuOption:
                      AvailabilityStatus: null
                  Source:
                    SheetImageStaticFileSource:
                      StaticFileId: '{{ StaticFileId }}'
                  ImageContentAltText: '{{ ImageContentAltText }}'
              SheetControlLayouts:
                - Configuration:
                    GridLayout: null
              Title: '{{ Title }}'
              Visuals:
                - FunnelChartVisual:
                    Subtitle:
                      Visibility: null
                      FormatText:
                        RichText: '{{ RichText }}'
                        PlainText: '{{ PlainText }}'
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        CategoryItemsLimit:
                          ItemsLimit: null
                          OtherCategories: '{{ OtherCategories }}'
                        CategorySort:
                          - FieldSort:
                              FieldId: '{{ FieldId }}'
                              Direction: null
                            ColumnSort:
                              AggregationFunction: null
                              SortBy: null
                              Direction: null
                      DataLabelOptions:
                        MeasureLabelVisibility: null
                        Position: '{{ Position }}'
                        Visibility: null
                        CategoryLabelVisibility: null
                        LabelColor: '{{ LabelColor }}'
                        MeasureDataLabelStyle: '{{ MeasureDataLabelStyle }}'
                        LabelFontConfiguration: null
                      CategoryLabelOptions:
                        Visibility: null
                        SortIconVisibility: null
                        AxisLabelOptions:
                          - CustomLabel: '{{ CustomLabel }}'
                            ApplyTo:
                              Column: null
                              FieldId: '{{ FieldId }}'
                            FontConfiguration: null
                      FieldWells:
                        FunnelChartAggregatedFieldWells:
                          Category:
                            - DateDimensionField:
                                HierarchyId: '{{ HierarchyId }}'
                                FormatConfiguration: null
                                Column: null
                                FieldId: '{{ FieldId }}'
                                DateGranularity: null
                              NumericalDimensionField:
                                HierarchyId: '{{ HierarchyId }}'
                                FormatConfiguration: null
                                Column: null
                                FieldId: '{{ FieldId }}'
                              CategoricalDimensionField:
                                HierarchyId: '{{ HierarchyId }}'
                                FormatConfiguration: null
                                Column: null
                                FieldId: '{{ FieldId }}'
                          Values:
                            - DateMeasureField:
                                AggregationFunction: null
                                FormatConfiguration: null
                                Column: null
                                FieldId: '{{ FieldId }}'
                              NumericalMeasureField:
                                AggregationFunction: null
                                FormatConfiguration: null
                                Column: null
                                FieldId: '{{ FieldId }}'
                              CategoricalMeasureField:
                                AggregationFunction: null
                                FormatConfiguration: null
                                Column: null
                                FieldId: '{{ FieldId }}'
                              CalculatedMeasureField:
                                Expression: '{{ Expression }}'
                                FieldId: '{{ FieldId }}'
                      Tooltip:
                        SelectedTooltipType: '{{ SelectedTooltipType }}'
                        TooltipVisibility: null
                        FieldBasedTooltip:
                          TooltipFields:
                            - FieldTooltipItem:
                                TooltipTarget: '{{ TooltipTarget }}'
                                FieldId: '{{ FieldId }}'
                                Label: '{{ Label }}'
                                Visibility: null
                              ColumnTooltipItem:
                                Aggregation: null
                                TooltipTarget: null
                                Column: null
                                Label: '{{ Label }}'
                                Visibility: null
                          AggregationVisibility: null
                          TooltipTitleType: '{{ TooltipTitleType }}'
                      ValueLabelOptions: null
                      VisualPalette:
                        ChartColor: '{{ ChartColor }}'
                        ColorMap:
                          - Element:
                              DataPathType:
                                PivotTableDataPathType: '{{ PivotTableDataPathType }}'
                              FieldId: '{{ FieldId }}'
                              FieldValue: '{{ FieldValue }}'
                            Color: '{{ Color }}'
                            TimeGranularity: null
                    Actions:
                      - Status: null
                        Trigger: '{{ Trigger }}'
                        CustomActionId: '{{ CustomActionId }}'
                        Name: '{{ Name }}'
                        ActionOperations:
                          - NavigationOperation: null
                            SetParametersOperation: null
                            FilterOperation:
                              SelectedFieldsConfiguration:
                                SelectedColumns:
                                  - null
                                SelectedFields:
                                  - '{{ SelectedFields[0] }}'
                                SelectedFieldOptions: '{{ SelectedFieldOptions }}'
                              TargetVisualsConfiguration:
                                SameSheetTargetVisualConfiguration:
                                  TargetVisualOptions: '{{ TargetVisualOptions }}'
                                  TargetVisuals:
                                    - '{{ TargetVisuals[0] }}'
                            URLOperation: null
                    Title:
                      Visibility: null
                      FormatText:
                        RichText: '{{ RichText }}'
                        PlainText: '{{ PlainText }}'
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - DateTimeHierarchy:
                          HierarchyId: '{{ HierarchyId }}'
                          DrillDownFilters:
                            - NumericEqualityFilter:
                                Column: null
                                Value: null
                              TimeRangeFilter:
                                Column: null
                                RangeMinimum: '{{ RangeMinimum }}'
                                TimeGranularity: null
                                RangeMaximum: '{{ RangeMaximum }}'
                              CategoryFilter:
                                Column: null
                                CategoryValues:
                                  - '{{ CategoryValues[0] }}'
                        ExplicitHierarchy:
                          HierarchyId: '{{ HierarchyId }}'
                          DrillDownFilters:
                            - null
                          Columns:
                            - null
                        PredefinedHierarchy:
                          HierarchyId: '{{ HierarchyId }}'
                          DrillDownFilters:
                            - null
                          Columns:
                            - null
                  BoxPlotVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        CategorySort:
                          - null
                        PaginationConfiguration:
                          PageSize: null
                          PageNumber: null
                      Legend:
                        Position: '{{ Position }}'
                        ValueFontConfiguration: null
                        Title: null
                        Visibility: null
                        Height: '{{ Height }}'
                        Width: '{{ Width }}'
                      ReferenceLines:
                        - Status: null
                          DataConfiguration:
                            DynamicConfiguration:
                              Column: null
                              MeasureAggregationFunction: null
                              Calculation: null
                            AxisBinding: '{{ AxisBinding }}'
                            SeriesType: '{{ SeriesType }}'
                            StaticConfiguration:
                              Value: null
                          LabelConfiguration:
                            HorizontalPosition: '{{ HorizontalPosition }}'
                            ValueLabelConfiguration:
                              FormatConfiguration: null
                              RelativePosition: '{{ RelativePosition }}'
                            CustomLabelConfiguration:
                              CustomLabel: '{{ CustomLabel }}'
                            FontColor: '{{ FontColor }}'
                            FontConfiguration: null
                            VerticalPosition: '{{ VerticalPosition }}'
                          StyleConfiguration:
                            Pattern: '{{ Pattern }}'
                            Color: '{{ Color }}'
                      CategoryAxis:
                        DataOptions:
                          DateAxisOptions:
                            MissingDateVisibility: null
                          NumericAxisOptions:
                            Scale:
                              Logarithmic:
                                Base: null
                              Linear:
                                StepSize: null
                                StepCount: null
                            Range:
                              DataDriven: {}
                              MinMax:
                                Minimum: null
                                Maximum: null
                        TickLabelOptions:
                          RotationAngle: null
                          LabelOptions: null
                        AxisOffset: '{{ AxisOffset }}'
                        AxisLineVisibility: null
                        GridLineVisibility: null
                        ScrollbarOptions:
                          VisibleRange:
                            PercentRange:
                              From: null
                              To: null
                          Visibility: null
                      PrimaryYAxisLabelOptions: null
                      CategoryLabelOptions: null
                      FieldWells:
                        BoxPlotAggregatedFieldWells:
                          GroupBy:
                            - null
                          Values:
                            - null
                      Tooltip: null
                      BoxPlotOptions:
                        StyleOptions:
                          FillStyle: '{{ FillStyle }}'
                        OutlierVisibility: null
                        AllDataPointsVisibility: null
                      PrimaryYAxisDisplayOptions: null
                      VisualPalette: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  GeospatialMapVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      Legend: null
                      MapStyleOptions:
                        BaseMapStyle: '{{ BaseMapStyle }}'
                      FieldWells:
                        GeospatialMapAggregatedFieldWells:
                          Colors:
                            - null
                          Values:
                            - null
                          Geospatial:
                            - null
                      Tooltip: null
                      WindowOptions:
                        Bounds:
                          West: null
                          South: null
                          North: null
                          East: null
                        MapZoomMode: '{{ MapZoomMode }}'
                      PointStyleOptions:
                        SelectedPointStyle: '{{ SelectedPointStyle }}'
                        ClusterMarkerConfiguration:
                          ClusterMarker:
                            SimpleClusterMarker:
                              Color: '{{ Color }}'
                        HeatmapConfiguration:
                          HeatmapColor:
                            Colors:
                              - Color: '{{ Color }}'
                      VisualPalette: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  ScatterPlotVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      YAxisLabelOptions: null
                      Legend: null
                      YAxisDisplayOptions: null
                      DataLabels:
                        DataLabelTypes:
                          - MaximumLabelType:
                              Visibility: null
                            DataPathLabelType:
                              FieldId: '{{ FieldId }}'
                              Visibility: null
                              FieldValue: '{{ FieldValue }}'
                            RangeEndsLabelType:
                              Visibility: null
                            FieldLabelType:
                              FieldId: '{{ FieldId }}'
                              Visibility: null
                            MinimumLabelType:
                              Visibility: null
                        MeasureLabelVisibility: null
                        Position: null
                        LabelContent: '{{ LabelContent }}'
                        Visibility: null
                        TotalsVisibility: null
                        Overlap: '{{ Overlap }}'
                        CategoryLabelVisibility: null
                        LabelColor: '{{ LabelColor }}'
                        LabelFontConfiguration: null
                      FieldWells:
                        ScatterPlotUnaggregatedFieldWells:
                          Category:
                            - null
                          Size:
                            - null
                          Label:
                            - null
                          XAxis:
                            - null
                          YAxis:
                            - null
                        ScatterPlotCategoricallyAggregatedFieldWells:
                          Category:
                            - null
                          Size:
                            - null
                          Label:
                            - null
                          XAxis:
                            - null
                          YAxis:
                            - null
                      Tooltip: null
                      XAxisLabelOptions: null
                      VisualPalette: null
                      XAxisDisplayOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  RadarChartVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        ColorSort:
                          - null
                        ColorItemsLimit: null
                        CategoryItemsLimit: null
                        CategorySort:
                          - null
                      Legend: null
                      Shape: '{{ Shape }}'
                      BaseSeriesSettings:
                        AreaStyleSettings:
                          Visibility: null
                      ColorLabelOptions: null
                      CategoryLabelOptions: null
                      AxesRangeScale: '{{ AxesRangeScale }}'
                      VisualPalette: null
                      AlternateBandColorsVisibility: null
                      StartAngle: null
                      CategoryAxis: null
                      FieldWells:
                        RadarChartAggregatedFieldWells:
                          Category:
                            - null
                          Color:
                            - null
                          Values:
                            - null
                      ColorAxis: null
                      AlternateBandOddColor: '{{ AlternateBandOddColor }}'
                      AlternateBandEvenColor: '{{ AlternateBandEvenColor }}'
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  ComboChartVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        ColorSort:
                          - null
                        ColorItemsLimit: null
                        CategoryItemsLimit: null
                        CategorySort:
                          - null
                      Legend: null
                      ReferenceLines:
                        - null
                      ColorLabelOptions: null
                      BarDataLabels: null
                      CategoryLabelOptions: null
                      Tooltip: null
                      SingleAxisOptions:
                        YAxisOptions:
                          YAxis: '{{ YAxis }}'
                      PrimaryYAxisDisplayOptions: null
                      VisualPalette: null
                      BarsArrangement: '{{ BarsArrangement }}'
                      SecondaryYAxisLabelOptions: null
                      LineDataLabels: null
                      CategoryAxis: null
                      PrimaryYAxisLabelOptions: null
                      FieldWells:
                        ComboChartAggregatedFieldWells:
                          BarValues:
                            - null
                          Category:
                            - null
                          Colors:
                            - null
                          LineValues:
                            - null
                      SecondaryYAxisDisplayOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  WordCloudVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        CategoryItemsLimit: null
                        CategorySort:
                          - null
                      CategoryLabelOptions: null
                      FieldWells:
                        WordCloudAggregatedFieldWells:
                          GroupBy:
                            - null
                          Size:
                            - null
                      WordCloudOptions:
                        WordOrientation: '{{ WordOrientation }}'
                        WordScaling: '{{ WordScaling }}'
                        CloudLayout: '{{ CloudLayout }}'
                        MaximumStringLength: null
                        WordCasing: '{{ WordCasing }}'
                        WordPadding: '{{ WordPadding }}'
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  SankeyDiagramVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        WeightSort:
                          - null
                        SourceItemsLimit: null
                        DestinationItemsLimit: null
                      DataLabels: null
                      FieldWells:
                        SankeyDiagramAggregatedFieldWells:
                          Destination:
                            - null
                          Source:
                            - null
                          Weight:
                            - null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  GaugeChartVisual:
                    Subtitle: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Arc:
                            ForegroundColor:
                              Gradient:
                                Expression: '{{ Expression }}'
                                Color:
                                  Stops:
                                    - GradientOffset: null
                                      DataValue: null
                                      Color: '{{ Color }}'
                              Solid:
                                Expression: '{{ Expression }}'
                                Color: '{{ Color }}'
                          PrimaryValue:
                            TextColor: null
                            Icon:
                              CustomCondition:
                                Expression: '{{ Expression }}'
                                Color: '{{ Color }}'
                                DisplayConfiguration:
                                  IconDisplayOption: '{{ IconDisplayOption }}'
                                IconOptions:
                                  UnicodeIcon: '{{ UnicodeIcon }}'
                                  Icon: '{{ Icon }}'
                              IconSet:
                                Expression: '{{ Expression }}'
                                IconSetType: '{{ IconSetType }}'
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      DataLabels: null
                      FieldWells:
                        TargetValues:
                          - null
                        Values:
                          - null
                      TooltipOptions: null
                      GaugeChartOptions:
                        Arc:
                          ArcAngle: null
                          ArcThickness: '{{ ArcThickness }}'
                        Comparison:
                          ComparisonMethod: '{{ ComparisonMethod }}'
                          ComparisonFormat:
                            NumberDisplayFormatConfiguration: null
                            PercentageDisplayFormatConfiguration: null
                        PrimaryValueDisplayType: '{{ PrimaryValueDisplayType }}'
                        ArcAxis:
                          Range:
                            Min: null
                            Max: null
                          ReserveRange: null
                        PrimaryValueFontConfiguration: null
                      VisualPalette: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  FilledMapVisual:
                    Subtitle: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Shape:
                            Format:
                              BackgroundColor: null
                            FieldId: '{{ FieldId }}'
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        CategorySort:
                          - null
                      Legend: null
                      MapStyleOptions: null
                      FieldWells:
                        FilledMapAggregatedFieldWells:
                          Values:
                            - null
                          Geospatial:
                            - null
                      Tooltip: null
                      WindowOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  WaterfallVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      CategoryAxisLabelOptions: null
                      SortConfiguration:
                        BreakdownItemsLimit: null
                        CategorySort:
                          - null
                      Legend: null
                      DataLabels: null
                      PrimaryYAxisLabelOptions: null
                      FieldWells:
                        WaterfallChartAggregatedFieldWells:
                          Categories:
                            - null
                          Breakdowns:
                            - null
                          Values:
                            - null
                      WaterfallChartOptions:
                        TotalBarLabel: '{{ TotalBarLabel }}'
                      ColorConfiguration:
                        GroupColorConfiguration:
                          NegativeBarColor: '{{ NegativeBarColor }}'
                          TotalBarColor: '{{ TotalBarColor }}'
                          PositiveBarColor: '{{ PositiveBarColor }}'
                      CategoryAxisDisplayOptions: null
                      PrimaryYAxisDisplayOptions: null
                      VisualPalette: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  CustomContentVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      ContentUrl: '{{ ContentUrl }}'
                      ContentType: '{{ ContentType }}'
                      ImageScaling: '{{ ImageScaling }}'
                    Actions:
                      - null
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  PieChartVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        SmallMultiplesSort:
                          - null
                        CategoryItemsLimit: null
                        CategorySort:
                          - null
                        SmallMultiplesLimitConfiguration: null
                      Legend: null
                      DataLabels: null
                      ContributionAnalysisDefaults:
                        - MeasureFieldId: '{{ MeasureFieldId }}'
                          ContributorDimensions:
                            - null
                      CategoryLabelOptions: null
                      FieldWells:
                        PieChartAggregatedFieldWells:
                          Category:
                            - null
                          Values:
                            - null
                          SmallMultiples:
                            - null
                      Tooltip: null
                      DonutOptions:
                        DonutCenterOptions:
                          LabelVisibility: null
                        ArcOptions:
                          ArcThickness: '{{ ArcThickness }}'
                      SmallMultiplesOptions:
                        MaxVisibleRows: null
                        PanelConfiguration:
                          BorderThickness: '{{ BorderThickness }}'
                          BorderStyle: '{{ BorderStyle }}'
                          GutterSpacing: '{{ GutterSpacing }}'
                          BackgroundVisibility: null
                          BorderVisibility: null
                          BorderColor: '{{ BorderColor }}'
                          Title:
                            Visibility: null
                            FontConfiguration: null
                            HorizontalTextAlignment: '{{ HorizontalTextAlignment }}'
                          GutterVisibility: null
                          BackgroundColor: '{{ BackgroundColor }}'
                        MaxVisibleColumns: null
                        XAxis:
                          Placement: '{{ Placement }}'
                          Scale: '{{ Scale }}'
                        YAxis: null
                      ValueLabelOptions: null
                      VisualPalette: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  KPIVisual:
                    Subtitle: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - PrimaryValue:
                            TextColor: null
                            Icon: null
                          ActualValue:
                            TextColor: null
                            Icon: null
                          ComparisonValue:
                            TextColor: null
                            Icon: null
                          ProgressBar:
                            ForegroundColor: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        TrendGroupSort:
                          - null
                      KPIOptions:
                        SecondaryValueFontConfiguration: null
                        VisualLayoutOptions:
                          StandardLayout:
                            Type: '{{ Type }}'
                        TrendArrows:
                          Visibility: null
                        SecondaryValue:
                          Visibility: null
                        Comparison: null
                        PrimaryValueDisplayType: null
                        ProgressBar:
                          Visibility: null
                        PrimaryValueFontConfiguration: null
                        Sparkline:
                          Type: '{{ Type }}'
                          Color: '{{ Color }}'
                          TooltipVisibility: null
                          Visibility: null
                      FieldWells:
                        TargetValues:
                          - null
                        TrendGroups:
                          - null
                        Values:
                          - null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  HistogramVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      YAxisDisplayOptions: null
                      DataLabels: null
                      BinOptions:
                        BinWidth:
                          BinCountLimit: null
                          Value: null
                        StartValue: null
                        SelectedBinType: '{{ SelectedBinType }}'
                        BinCount:
                          Value: null
                      FieldWells:
                        HistogramAggregatedFieldWells:
                          Values:
                            - null
                      Tooltip: null
                      XAxisLabelOptions: null
                      VisualPalette: null
                      XAxisDisplayOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  PluginVisual:
                    Subtitle: null
                    PluginArn: '{{ PluginArn }}'
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        PluginVisualTableQuerySort:
                          ItemsLimitConfiguration:
                            ItemsLimit: null
                          RowSort:
                            - null
                      VisualOptions:
                        VisualProperties:
                          - Value: '{{ Value }}'
                            Name: '{{ Name }}'
                      FieldWells:
                        - Unaggregated:
                            - FormatConfiguration: null
                              Column: null
                              FieldId: '{{ FieldId }}'
                          AxisName: '{{ AxisName }}'
                          Measures:
                            - null
                          Dimensions:
                            - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  TableVisual:
                    Subtitle: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Row:
                            TextColor: null
                            BackgroundColor: null
                          Cell:
                            FieldId: '{{ FieldId }}'
                            TextFormat:
                              TextColor: null
                              Icon: null
                              BackgroundColor: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        RowSort:
                          - null
                        PaginationConfiguration: null
                      PaginatedReportOptions:
                        OverflowColumnHeaderVisibility: null
                        VerticalOverflowVisibility: null
                      TableOptions:
                        HeaderStyle:
                          VerticalTextAlignment: '{{ VerticalTextAlignment }}'
                          Visibility: null
                          Height: null
                          FontConfiguration: null
                          Border:
                            UniformBorder:
                              Thickness: null
                              Color: '{{ Color }}'
                              Style: '{{ Style }}'
                            SideSpecificBorder:
                              Left: null
                              Top: null
                              InnerHorizontal: null
                              Right: null
                              Bottom: null
                              InnerVertical: null
                          TextWrap: '{{ TextWrap }}'
                          HorizontalTextAlignment: null
                          BackgroundColor: '{{ BackgroundColor }}'
                        CellStyle: null
                        Orientation: '{{ Orientation }}'
                        RowAlternateColorOptions:
                          Status: null
                          UsePrimaryBackgroundColor: null
                          RowAlternateColors:
                            - '{{ RowAlternateColors[0] }}'
                      TableInlineVisualizations:
                        - DataBars:
                            PositiveColor: '{{ PositiveColor }}'
                            FieldId: '{{ FieldId }}'
                            NegativeColor: '{{ NegativeColor }}'
                      FieldWells:
                        TableUnaggregatedFieldWells:
                          Values:
                            - null
                        TableAggregatedFieldWells:
                          GroupBy:
                            - null
                          Values:
                            - null
                      FieldOptions:
                        Order:
                          - '{{ Order[0] }}'
                        PinnedFieldOptions:
                          PinnedLeftFields:
                            - '{{ PinnedLeftFields[0] }}'
                        SelectedFieldOptions:
                          - CustomLabel: '{{ CustomLabel }}'
                            URLStyling:
                              LinkConfiguration:
                                Target: null
                                Content:
                                  CustomIconContent:
                                    Icon: '{{ Icon }}'
                                  CustomTextContent:
                                    Value: '{{ Value }}'
                                    FontConfiguration: null
                              ImageConfiguration:
                                SizingOptions:
                                  TableCellImageScalingConfiguration: '{{ TableCellImageScalingConfiguration }}'
                            FieldId: '{{ FieldId }}'
                            Visibility: null
                            Width: '{{ Width }}'
                      TotalOptions:
                        TotalAggregationOptions:
                          - TotalAggregationFunction:
                              SimpleTotalAggregationFunction: '{{ SimpleTotalAggregationFunction }}'
                            FieldId: '{{ FieldId }}'
                        CustomLabel: '{{ CustomLabel }}'
                        ScrollStatus: '{{ ScrollStatus }}'
                        Placement: '{{ Placement }}'
                        TotalCellStyle: null
                        TotalsVisibility: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  PivotTableVisual:
                    Subtitle: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Cell:
                            Scope:
                              Role: '{{ Role }}'
                            Scopes:
                              - null
                            FieldId: '{{ FieldId }}'
                            TextFormat: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        FieldSortOptions:
                          - SortBy:
                              Field: null
                              DataPath:
                                SortPaths:
                                  - null
                                Direction: null
                              Column: null
                            FieldId: '{{ FieldId }}'
                      PaginatedReportOptions:
                        OverflowColumnHeaderVisibility: null
                        VerticalOverflowVisibility: null
                      TableOptions:
                        RowFieldNamesStyle: null
                        RowHeaderStyle: null
                        CollapsedRowDimensionsVisibility: null
                        RowsLayout: '{{ RowsLayout }}'
                        MetricPlacement: '{{ MetricPlacement }}'
                        DefaultCellWidth: '{{ DefaultCellWidth }}'
                        ColumnNamesVisibility: null
                        RowsLabelOptions:
                          CustomLabel: '{{ CustomLabel }}'
                          Visibility: null
                        SingleMetricVisibility: null
                        ColumnHeaderStyle: null
                        ToggleButtonsVisibility: null
                        CellStyle: null
                        RowAlternateColorOptions: null
                      FieldWells:
                        PivotTableAggregatedFieldWells:
                          Values:
                            - null
                          Columns:
                            - null
                          Rows:
                            - null
                      FieldOptions:
                        CollapseStateOptions:
                          - Target:
                              FieldId: '{{ FieldId }}'
                              FieldDataPathValues:
                                - null
                            State: '{{ State }}'
                        DataPathOptions:
                          - DataPathList:
                              - null
                            Width: '{{ Width }}'
                        SelectedFieldOptions:
                          - CustomLabel: '{{ CustomLabel }}'
                            FieldId: '{{ FieldId }}'
                            Visibility: null
                      TotalOptions:
                        ColumnSubtotalOptions:
                          CustomLabel: '{{ CustomLabel }}'
                          FieldLevelOptions:
                            - FieldId: '{{ FieldId }}'
                          ValueCellStyle: null
                          TotalCellStyle: null
                          TotalsVisibility: null
                          FieldLevel: '{{ FieldLevel }}'
                          MetricHeaderCellStyle: null
                          StyleTargets:
                            - CellType: '{{ CellType }}'
                        RowSubtotalOptions: null
                        RowTotalOptions:
                          TotalAggregationOptions:
                            - null
                          CustomLabel: '{{ CustomLabel }}'
                          ValueCellStyle: null
                          ScrollStatus: null
                          Placement: null
                          TotalCellStyle: null
                          TotalsVisibility: null
                          MetricHeaderCellStyle: null
                        ColumnTotalOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  BarChartVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        SmallMultiplesSort:
                          - null
                        ColorSort:
                          - null
                        ColorItemsLimit: null
                        CategoryItemsLimit: null
                        CategorySort:
                          - null
                        SmallMultiplesLimitConfiguration: null
                      Legend: null
                      ReferenceLines:
                        - null
                      DataLabels: null
                      ColorLabelOptions: null
                      CategoryLabelOptions: null
                      Tooltip: null
                      SmallMultiplesOptions: null
                      Orientation: '{{ Orientation }}'
                      VisualPalette: null
                      ValueLabelOptions: null
                      BarsArrangement: null
                      CategoryAxis: null
                      ContributionAnalysisDefaults:
                        - null
                      FieldWells:
                        BarChartAggregatedFieldWells:
                          Category:
                            - null
                          Colors:
                            - null
                          Values:
                            - null
                          SmallMultiples:
                            - null
                      ValueAxis: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  HeatMapVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        HeatMapRowSort:
                          - null
                        HeatMapRowItemsLimitConfiguration: null
                        HeatMapColumnItemsLimitConfiguration: null
                        HeatMapColumnSort:
                          - null
                      ColumnLabelOptions: null
                      Legend: null
                      DataLabels: null
                      FieldWells:
                        HeatMapAggregatedFieldWells:
                          Values:
                            - null
                          Columns:
                            - null
                          Rows:
                            - null
                      Tooltip: null
                      ColorScale:
                        Colors:
                          - DataValue: null
                            Color: '{{ Color }}'
                        ColorFillType: '{{ ColorFillType }}'
                        NullValueColor: null
                      RowLabelOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  TreeMapVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        TreeMapSort:
                          - null
                        TreeMapGroupItemsLimitConfiguration: null
                      Legend: null
                      DataLabels: null
                      ColorLabelOptions: null
                      SizeLabelOptions: null
                      FieldWells:
                        TreeMapAggregatedFieldWells:
                          Sizes:
                            - null
                          Colors:
                            - null
                          Groups:
                            - null
                      Tooltip: null
                      ColorScale: null
                      GroupLabelOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  InsightVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    Actions:
                      - null
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                    InsightConfiguration:
                      Computations:
                        - PeriodToDate:
                            PeriodTimeGranularity: null
                            Value: null
                            Time: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          GrowthRate:
                            Value: null
                            Time: null
                            PeriodSize: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          TopBottomRanked:
                            Type: '{{ Type }}'
                            Category: null
                            ResultSize: null
                            Value: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          TotalAggregation:
                            Value: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          Forecast:
                            PeriodsBackward: null
                            PeriodsForward: null
                            PredictionInterval: null
                            Seasonality: '{{ Seasonality }}'
                            CustomSeasonalityValue: null
                            Value: null
                            Time: null
                            UpperBoundary: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            LowerBoundary: null
                          MaximumMinimum:
                            Type: '{{ Type }}'
                            Value: null
                            Time: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          PeriodOverPeriod:
                            Value: null
                            Time: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          MetricComparison:
                            TargetValue: null
                            Time: null
                            ComputationId: '{{ ComputationId }}'
                            FromValue: null
                            Name: '{{ Name }}'
                          TopBottomMovers:
                            Type: null
                            Category: null
                            Value: null
                            SortOrder: '{{ SortOrder }}'
                            Time: null
                            MoverSize: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                          UniqueValues:
                            Category: null
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                      CustomNarrative:
                        Narrative: '{{ Narrative }}'
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                  LineChartVisual:
                    Subtitle: null
                    VisualId: '{{ VisualId }}'
                    ChartConfiguration:
                      SortConfiguration:
                        CategoryItemsLimitConfiguration: null
                        ColorItemsLimitConfiguration: null
                        SmallMultiplesSort:
                          - null
                        CategorySort:
                          - null
                        SmallMultiplesLimitConfiguration: null
                      Legend: null
                      ReferenceLines:
                        - null
                      DataLabels: null
                      Tooltip: null
                      SingleAxisOptions: null
                      SmallMultiplesOptions: null
                      PrimaryYAxisDisplayOptions:
                        MissingDataConfigurations:
                          - TreatmentOption: '{{ TreatmentOption }}'
                        AxisOptions: null
                      VisualPalette: null
                      XAxisDisplayOptions: null
                      DefaultSeriesSettings:
                        LineStyleSettings:
                          LineInterpolation: '{{ LineInterpolation }}'
                          LineStyle: '{{ LineStyle }}'
                          LineVisibility: null
                          LineWidth: '{{ LineWidth }}'
                        AxisBinding: null
                        MarkerStyleSettings:
                          MarkerShape: '{{ MarkerShape }}'
                          MarkerSize: '{{ MarkerSize }}'
                          MarkerVisibility: null
                          MarkerColor: '{{ MarkerColor }}'
                      SecondaryYAxisLabelOptions: null
                      ForecastConfigurations:
                        - ForecastProperties:
                            PeriodsBackward: null
                            PeriodsForward: null
                            PredictionInterval: null
                            Seasonality: null
                            UpperBoundary: null
                            LowerBoundary: null
                          Scenario:
                            WhatIfRangeScenario:
                              StartDate: '{{ StartDate }}'
                              Value: null
                              EndDate: '{{ EndDate }}'
                            WhatIfPointScenario:
                              Value: null
                              Date: '{{ Date }}'
                      Series:
                        - FieldSeriesItem:
                            FieldId: '{{ FieldId }}'
                            AxisBinding: null
                            Settings:
                              LineStyleSettings: null
                              MarkerStyleSettings: null
                          DataFieldSeriesItem:
                            FieldId: '{{ FieldId }}'
                            AxisBinding: null
                            FieldValue: '{{ FieldValue }}'
                            Settings: null
                      Type: '{{ Type }}'
                      PrimaryYAxisLabelOptions: null
                      ContributionAnalysisDefaults:
                        - null
                      FieldWells:
                        LineChartAggregatedFieldWells:
                          Category:
                            - null
                          Colors:
                            - null
                          Values:
                            - null
                          SmallMultiples:
                            - null
                      SecondaryYAxisDisplayOptions: null
                      XAxisLabelOptions: null
                    Actions:
                      - null
                    Title: null
                    VisualContentAltText: '{{ VisualContentAltText }}'
                    ColumnHierarchies:
                      - null
                  EmptyVisual:
                    VisualId: '{{ VisualId }}'
                    Actions:
                      - null
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
              Name: '{{ Name }}'
          ParameterDeclarations:
            - StringParameterDeclaration:
                MappedDataSetParameters:
                  - DataSetParameterName: '{{ DataSetParameterName }}'
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                DefaultValues:
                  DynamicValue:
                    GroupNameColumn: null
                    DefaultValueColumn: null
                    UserNameColumn: null
                  StaticValues:
                    - '{{ StaticValues[0] }}'
                ParameterValueType: '{{ ParameterValueType }}'
                ValueWhenUnset:
                  ValueWhenUnsetOption: '{{ ValueWhenUnsetOption }}'
                  CustomValue: '{{ CustomValue }}'
                Name: '{{ Name }}'
              DateTimeParameterDeclaration:
                MappedDataSetParameters:
                  - null
                DefaultValues:
                  RollingDate: null
                  DynamicValue: null
                  StaticValues:
                    - '{{ StaticValues[0] }}'
                TimeGranularity: null
                ValueWhenUnset:
                  ValueWhenUnsetOption: null
                  CustomValue: '{{ CustomValue }}'
                Name: '{{ Name }}'
              DecimalParameterDeclaration:
                MappedDataSetParameters:
                  - null
                DefaultValues:
                  DynamicValue: null
                  StaticValues:
                    - null
                ParameterValueType: null
                ValueWhenUnset:
                  ValueWhenUnsetOption: null
                  CustomValue: null
                Name: '{{ Name }}'
              IntegerParameterDeclaration:
                MappedDataSetParameters:
                  - null
                DefaultValues:
                  DynamicValue: null
                  StaticValues:
                    - null
                ParameterValueType: null
                ValueWhenUnset:
                  ValueWhenUnsetOption: null
                  CustomValue: null
                Name: '{{ Name }}'
      - name: ValidationStrategy
        value:
          Mode: '{{ Mode }}'
      - name: FolderArns
        value:
          - '{{ FolderArns[0] }}'
      - name: DashboardId
        value: '{{ DashboardId }}'
      - name: LinkSharingConfiguration
        value:
          Permissions:
            - Principal: '{{ Principal }}'
              Actions:
                - '{{ Actions[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: DashboardPublishOptions
        value:
          SheetControlsOption:
            VisibilityState: '{{ VisibilityState }}'
          ExportToCSVOption:
            AvailabilityStatus: '{{ AvailabilityStatus }}'
          DataPointMenuLabelOption:
            AvailabilityStatus: null
          DataPointDrillUpDownOption:
            AvailabilityStatus: null
          AdHocFilteringOption:
            AvailabilityStatus: null
          VisualPublishOptions:
            ExportHiddenFieldsOption:
              AvailabilityStatus: null
          VisualMenuOption: null
          DataPointTooltipOption:
            AvailabilityStatus: null
          VisualAxisSortOption:
            AvailabilityStatus: null
          ExportWithHiddenFieldsOption:
            AvailabilityStatus: null
          SheetLayoutElementMaximizationOption:
            AvailabilityStatus: null
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: Permissions
        value:
          - null
      - name: LinkEntities
        value:
          - '{{ LinkEntities[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.quicksight.dashboards
WHERE data__Identifier = '<AwsAccountId|DashboardId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dashboards</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeDashboard,
quicksight:DescribeDashboardPermissions,
quicksight:ListTagsForResource
```

### Create
```json
quicksight:DescribeDashboard,
quicksight:DescribeDashboardPermissions,
quicksight:CreateDashboard,
quicksight:DescribeTemplate,
quicksight:DescribeTheme,
quicksight:PassDataSet,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource,
quicksight:CreateFolderMembership,
quicksight:DeleteFolderMembership,
quicksight:ListFoldersForResource
```

### Update
```json
quicksight:DescribeDashboard,
quicksight:DescribeDashboardPermissions,
quicksight:UpdateDashboard,
quicksight:UpdateDashboardLinks,
quicksight:UpdateDashboardPermissions,
quicksight:UpdateDashboardPublishedVersion,
quicksight:DescribeTemplate,
quicksight:DescribeTheme,
quicksight:PassDataSet,
quicksight:CreateFolderMembership,
quicksight:DeleteFolderMembership,
quicksight:ListFoldersForResource,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### List
```json
quicksight:ListDashboards
```

### Delete
```json
quicksight:DescribeDashboard,
quicksight:DeleteDashboard
```
