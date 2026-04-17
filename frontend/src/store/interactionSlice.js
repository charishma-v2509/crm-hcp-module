import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  hcps: [],
  currentInteraction: {
    hcp_id: '',
    interaction_type: 'Meeting',
    date: '',
    time: '',
    attendees: '',
    topics_discussed: '',
    materials_shared: '',
    samples_distributed: '',
    sentiment: 'Neutral',
    outcomes: '',
    follow_up_actions: '',
  },
  aiSummary: '',
  aiSuggestions: '',
  loading: false,
  error: '',
  success: '',
  chatMessages: [
    {
      role: 'ai',
      text: 'Hi! I am your AI assistant. Log interaction details here or ask for help.',
    },
  ],
};

const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {
    setHCPs: (state, action) => {
      state.hcps = action.payload;
    },
    updateField: (state, action) => {
      const { field, value } = action.payload;
      state.currentInteraction[field] = value;
    },
    setAISummary: (state, action) => {
      state.aiSummary = action.payload;
    },
    setAISuggestions: (state, action) => {
      state.aiSuggestions = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    },
    setSuccess: (state, action) => {
      state.success = action.payload;
    },
    addChatMessage: (state, action) => {
      state.chatMessages.push(action.payload);
    },
    resetForm: (state) => {
      state.currentInteraction = initialState.currentInteraction;
      state.aiSummary = '';
      state.aiSuggestions = '';
      state.error = '';
      state.success = '';
    },
  },
});

export const {
  setHCPs,
  updateField,
  setAISummary,
  setAISuggestions,
  setLoading,
  setError,
  setSuccess,
  addChatMessage,
  resetForm,
} = interactionSlice.actions;

export default interactionSlice.reducer;